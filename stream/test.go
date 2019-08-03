// What it does:
//
// This example uses the VideoCapture class to capture a frame from a connected webcam,
// then save it to an image file on disk.
//
// How to run:
//
// saveimage [camera ID] [image file]
//
// 		go run ./cmd/saveimage/main.go 0 filename.jpg
//
// +build example

package main

import (
	"fmt"
	"os"
	"strconv"
	"time"

	"gocv.io/x/gocv"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("How to run:\n\tsaveimage [camera ID] [image file]")
		return
	}

	deviceID := os.Args[1]

	webcam, err := gocv.OpenVideoCapture(deviceID)
	if err != nil {
		fmt.Printf("Error opening video capture device: %v\n", deviceID)
		return
	}
	defer webcam.Close()

	img := gocv.NewMat()
	start := time.Now()
	elapsed := time.Since(start)

	defer img.Close()
	for i := 0; i < 100; i++ {
		if ok := webcam.Read(&img); !ok {
			fmt.Printf("cannot read device %v\n", deviceID)
			return
		}
		if img.Empty() {
			fmt.Printf("no image on device %v\n", deviceID)
			return
		}
		num := strconv.Itoa(i)
		saveFile := num + ".jpg"
		gocv.IMWrite(saveFile, img)

		fmt.Println(num)

	}

}
