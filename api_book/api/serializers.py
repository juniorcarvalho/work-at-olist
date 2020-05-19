from rest_framework import serializers

from api_book.core.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    '''
    serializer for Author model
    '''

    class Meta:
        model = Author
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    '''
    serializer for Book model
    '''
    authors = AuthorSerializer(many=True, read_only=True)
    authors_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(),
                                                    write_only=True, many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'edition', 'publication_year', 'authors', 'authors_id')

    def create(self, validated_data):
        authors_id = validated_data.pop('authors_id')
        book = Book.objects.create(**validated_data)
        for author in authors_id:
            book.authors.add(author)
        return book

    def update(self, instance, validated_data):
        authors_id = validated_data.pop('authors_id')
        for existing_author in instance.authors.all():
            instance.authors.remove(existing_author)
        instance = super(BookSerializer, self).update(instance, validated_data)
        for author in authors_id:
            instance.authors.add(author)
        return instance
