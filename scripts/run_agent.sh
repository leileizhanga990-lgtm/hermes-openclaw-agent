#!/bin/bash

echo "🚀 Starting Hermes + OpenClaw Agent System..."

# Activate environment (optional)
# source venv/bin/activate

echo "🔧 Initializing Agent Brain..."
sleep 1

echo "⚙️ Loading workflow configurations..."
sleep 1

echo "🌐 Connecting to model providers..."
sleep 1

echo "🧠 Agent is now running..."
echo "----------------------------------"

python3 -m core.agent_brain

echo "✅ System execution finished."
