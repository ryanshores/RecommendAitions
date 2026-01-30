import json
from unittest.mock import patch, MagicMock
from app.client.recommender import recommend

@patch('app.client.recommender.requests.post')
def test_recommend(mock_post):
    # Mock Ollama response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "model": "qwen2.5-coder:7b",
        "created_at": "2026-01-29T19:01:07.936915Z",
        "message": {
            "role": "assistant",
            "content": "Here are your recommendations..."
        },
        "done": True
    }
    mock_post.return_value = mock_response

    titles = [{"title": "Test Movie", "overview": "Test Overview"}]
    user_profile = {"max_results": 5, "likes": ["Test"], "dislikes": [], "tone": "test"}
    
    result = recommend(titles, user_profile)
    
    # Check if correct payload was sent
    args, kwargs = mock_post.call_args
    sent_json = kwargs['json']
    
    print(f"Sent JSON: {json.dumps(sent_json, indent=2)}")
    print(f"Result: {result}")
    
    assert sent_json["stream"] == False
    assert "messages" in sent_json
    assert result == "Here are your recommendations..."
    print("Test passed!")

if __name__ == "__main__":
    test_recommend()
