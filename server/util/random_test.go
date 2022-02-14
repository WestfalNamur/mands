package util

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestRandomString(t *testing.T) {
	s0 := RandomString(7)
	s1 := RandomString(7)

	require.NotEmpty(t, s0)
	require.NotEmpty(t, s1)
	require.NotEqual(t, s0, s1)
}
