import boto3


def delete_movie_table(dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')
    table.delete()


if __name__ == '__main__':
    delete_movie_table()
    print("Movies table deleted.")
