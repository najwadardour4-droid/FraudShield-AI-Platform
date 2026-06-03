import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models, transforms, datasets
from torch.utils.data import DataLoader

def train_model(data_dir: str, model_save_path: str, num_epochs: int = 10):
    """
    Train a CNN (ResNet18) to classify documents as AUTHENTIC or FAKE.
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # 1. Data Augmentation
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(10),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    # 2. Load Dataset
    # Expects data_dir/authentic and data_dir/fake
    try:
        dataset = datasets.ImageFolder(data_dir, transform=transform)
        dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return

    # 3. Define Model (Transfer Learning)
    model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 2) # Binary classification: 0=Authentic, 1=Fake
    model = model.to(device)
    
    # 4. Loss and Optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    # 5. Training Loop
    model.train()
    for epoch in range(num_epochs):
        running_loss = 0.0
        for inputs, labels in dataloader:
            inputs, labels = inputs.to(device), labels.to(device)
            
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
        
        print(f"Epoch {epoch+1}/{num_epochs}, Loss: {running_loss/len(dataloader):.4f}")
        
    # 6. Save Model
    torch.save(model.state_dict(), model_save_path)
    print(f"Model saved to {model_save_path}")

if __name__ == "__main__":
    # Example usage:
    # train_model('path/to/data', 'backend/ml_models/document_resnet.pt')
    pass
