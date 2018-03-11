# see https://stackoverflow.com/questions/2481269/how-to-make-a-simple-c-makefile
# https://stackoverflow.com/questions/7004702/how-can-i-create-a-makefile-for-c-projects-with-src-obj-and-bin-subdirectories
# https://stackoverflow.com/questions/2706064/compile-all-c-files-in-a-directory-into-separate-programs
# https://stackoverflow.com/questions/12605051/how-to-check-if-a-directory-doesnt-exist-in-make-and-create-it
TARGET 	:= webInterface.out

rwildcard=$(foreach d,$(wildcard $1*),$(call rwildcard,$d/,$2) $(filter $(subst *,%,$2),$d))

CXX 	:= g++
CPPFLAGS:= -std=c++11 -g -Wall
# LDFLAGS := -g $(shell root-config --ldflags)
LDLIBS 	:= -l bcm2835

RM 		:= rm -rf
SRC_DIR := ./
OBJDIR 	:= ./objs
SOURCES := $(call rwildcard,,*.cpp) #$(wildcard ./*/*.cpp)
# INCLUDES:= $(wildcard ./*/*.h)
OBJS 	:= $(subst .cpp, .o, $(SOURCES))
# OBJS 	:= $(patsubst .cpp, %.o, $(SOURCES))
PROGS 	:= $(patsubst %.cpp, %, $(SOURCES))

all: $(TARGET)

DEBUG_MAKE:
	@echo "HERE"
	@echo $(OBJS)

clean:
	$(RM) $(OBJS)

run: all
	./main.out

$(TARGET): $(PROGS)
	$(CXX) $(CPPFLAGS) $(wildcard $(OBJDIR)/*.o) -o $(TARGET)

%: %.cpp
	$(CXX) -c $(CPPFLAGS) $< -o $(OBJDIR)/$(basename $(notdir $@)).o

# $(TARGET): obj
# 	$(LINKER) $(TARGET) $(LFLAGS) $(OBJECTS)
# 	echo "Linking complete!"
#
# obj: $(SOURCES) $(INCLUDES)
# 	$(CXX) -c $(CPPFLAGS) $(SOURCES) -o $(OBJDIR)/
# 	echo "Compilation complete!"

# depend: .depend
#
# .depend: $(SOURCES)
# 	rm -f ./.depend
# 	$(CXX) $(CXXFLAGS) -MM $^>>./.depend;
#
# include .depend
