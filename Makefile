CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++17

TARGET = my-touch
SRC = my-touch.cpp

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: clean

