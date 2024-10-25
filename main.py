import os
import googleapiclient.discovery
from dotenv import load_dotenv
import csv


# Function to extract video ID from YouTube URL
def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1]
    else:
        raise ValueError("Link de YouTube inválido")


# Function to get comments using YouTube API
def get_video_comments(video_id, api_key):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    comments_data = []
    next_page_token = None

    while True:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            pageToken=next_page_token,
            maxResults=100,
        )
        response = request.execute()

        for item in response["items"]:
            comment_info = item["snippet"]["topLevelComment"]["snippet"]

            comment_data = {
                "textDisplay": comment_info["textDisplay"],
                "likeCount": comment_info["likeCount"],
                "authorDisplayName": comment_info["authorDisplayName"],
                "authorChannelUrl": comment_info["authorChannelUrl"],
                "authorChannelId": comment_info["authorChannelId"]["value"],
                "publishedAt": comment_info["publishedAt"],
                "updatedAt": comment_info["updatedAt"],
            }

            comments_data.append(comment_data)

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return comments_data


# Function to save comments to a CSV file in 'outputs/' directory
def save_comments_to_csv(comments_data, video_id):
    # Ensure 'outputs' directory exists
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    csv_filename = os.path.join(output_dir, f"{video_id}.csv")

    # Define the fields (columns) to be included in the CSV
    fieldnames = [
        "textDisplay",
        "likeCount",
        "authorDisplayName",
        "authorChannelUrl",
        "authorChannelId",
        "publishedAt",
        "updatedAt",
    ]

    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for comment_data in comments_data:
            writer.writerow(comment_data)

    print(f"✓ Comentarios guardados en {csv_filename}")


# Main function
def main():
    youtube_url = input("Ingresa el link de YouTube: ")
    load_dotenv()
    api_key = os.getenv("YOUTUBE_API_KEY")

    try:
        video_id = extract_video_id(youtube_url)
    except ValueError as e:
        print(e)
        return

    try:
        comments_data = get_video_comments(video_id, api_key)
        print(f"✓ Se extrajeron {len(comments_data)} comentarios del link: {youtube_url}")
        save_comments_to_csv(comments_data, video_id)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
