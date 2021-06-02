// 参考サイト
// https://www.youtube.com/watch?v=6ZjN46u2gYg
package main

import (
	"fmt"
	"strconv"
	"strings"
)

// 構造体を定義
type Station struct {
	Name  string
	Rapid int
	Next  *Station
}

// GOはコンストラクタがないのでNewで始まる関数を定義しその内部で構造体を生成するのが通例
func NewStation(name string, rapid int, next *Station) *Station {
	obj := &Station{
		Name:  name,
		Rapid: rapid,
		Next:  next,
	}
	return obj
}

// 構造体を定義
type LinkedList struct {
	Top *Station
}

func (obj *LinkedList) showLine() {
	top := obj.Top
	for {
		if top == nil {
			break
		}
		fmt.Printf("%v %v\n", top.Name, top.Rapid)
		top = top.Next
	}
}

func (obj *LinkedList) insert(n int, name string) {
	// n 番目に name を追加
	addObj := new(Station)
	addObj.Name = name

	oldObj := obj.Top
	preObj := new(Station)
	i := 1

	for {
		if n == 1 {
			addObj.Next = oldObj
			obj.Top = addObj
			break
		} else if i == n {
			addObj.Next = oldObj
			preObj.Next = addObj
			break
		}

		if oldObj.Name == "" {
			break
		}

		preObj = oldObj
		oldObj = oldObj.Next

		i++
	}
}

func (obj *LinkedList) delete(name string) {
	// name を削除
	tmpObj := obj.Top
	preObj := new(Station)

	for {
		if tmpObj.Name == name {
			if preObj.Name == "" {
				obj.Top = tmpObj.Next
			} else {
				preObj.Next = tmpObj.Next
			}
			break
		}

		if tmpObj.Name == "" {
			break
		}

		preObj = tmpObj
		tmpObj = tmpObj.Next
	}
}

func main() {
	defaultData := []string{
		"hachioji 1",
		"katakura 1",
		"hashimoto 1",
		"sagamihara 1",
		"yabe 0",
		"fuchinobe 0",
		"kobuchi 0",
		"machida 1",
	}

	lst := new(LinkedList)
	obj2 := new(Station)

	for _, v := range defaultData {
		s := strings.Split(v, " ")
		rapid, _ := strconv.Atoi(s[1])
		obj := NewStation(s[0], rapid, nil)
		if obj2.Name == "" {
			lst.Top = obj
		} else {
			obj2.Next = obj
		}
		obj2 = obj
	}

	lst.showLine()
	fmt.Println("-----------")
	// 追加
	lst.insert(9, "すすきの")
	lst.insert(1, "大通り")
	lst.insert(5, "中の島")
	lst.showLine()
	fmt.Println("-----------")
	// 削除
	lst.delete("すすきの")
	lst.delete("中の島")
	lst.delete("yabe")
	lst.showLine()
}

// hachioji 1
// katakura 1
// hashimoto 1
// sagamihara 1
// yabe 0
// fuchinobe 0
// kobuchi 0
// machida 1
// -----------
// 大通り 0
// hachioji 1
// katakura 1
// hashimoto 1
// 中の島 0
// sagamihara 1
// yabe 0
// fuchinobe 0
// kobuchi 0
// machida 1
// すすきの 0
// -----------
// 大通り 0
// hachioji 1
// katakura 1
// hashimoto 1
// sagamihara 1
// fuchinobe 0
// kobuchi 0
// machida 1
