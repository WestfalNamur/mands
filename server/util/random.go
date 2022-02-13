package util

import (
	"math/rand"
	"strings"
	"time"
)

const alphabet = "abcdefghijklmnopqrstuvwxyz"

func RandomString(n int) string {

	// Test seem to fail otherwise. Maybe due to caching?
	// See: https://pkg.go.dev/math/rand#Seed
	rand.Seed(time.Now().UnixNano())

	var sb strings.Builder
	k := len(alphabet)

	for i := 0; i < n; i++ {
		c := alphabet[rand.Intn(k)]
		sb.WriteByte(c)
	}

	return sb.String()
}

func RandomText(n int) string {

	var s []string

	for i := 0; i < n; i++ {
		rand.Seed(time.Now().UnixNano())
		v := rand.Intn(10) + 2
		str := RandomString(v)
		s = append(s, str)
	}

	return strings.Join(s, " ")
}
