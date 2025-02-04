[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/json-serialization.html)
  * [中文](/cn/current/Manual/json-serialization.html)
  * [日本語](/ja/current/Manual/json-serialization.html)
  * [한국어](/kr/current/Manual/json-serialization.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/json-serialization.html)
  * [中文](/cn/current/Manual/json-serialization.html)
  * [日本語](/ja/current/Manual/json-serialization.html)
  * [한국어](/kr/current/Manual/json-serialization.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script serialization](script-serialization.html)
  * JSON Serialization

[](script-serialization-how-unity-uses.html)

How Unity uses serialization

[](script-serialization-errors.html)

Script serialization errors

# JSON Serialization

Use the [JsonUtility](../ScriptReference/JsonUtility.html) class to convert
Unity objects to and from the [JSON](http://www.json.org) format. For example,
you can use JSON Serialization to interact with web services, or to easily
pack and unpack data to a text-based format.

JSON Serialization uses a notion of “structured” JSON: you create a class or
structure to describe what variables you want to store in your JSON data. For
example:

    
    
    [Serializable]
    public class MyClass
    {
        public int level;
        public float timeElapsed;
        public string playerName;
    }
    

This defines a plain C# class containing three variables (**level** ,
**timeElapsed** , and **playerName**) and marks it with the `Serializable`
attribute, in order to work with the JSON serializer. To create an instance of
your class, you can use something like this:

    
    
    MyClass myObject = new MyClass();
    myObject.level = 1;
    myObject.timeElapsed = 47.5f;
    myObject.playerName = "Dr Charles Francis";
    

Then use the [JsonUtility.ToJson](../ScriptReference/JsonUtility.ToJson.html)
method to serialize it (convert it) to the JSON format:

    
    
    string json = JsonUtility.ToJson(myObject);
    // json now contains: '{"level":1,"timeElapsed":47.5,"playerName":"Dr Charles Francis"}'
    

To convert the JSON back into an object, use
[JsonUtility.FromJson](../ScriptReference/JsonUtility.FromJson.html):

    
    
    myObject = JsonUtility.FromJson<MyClass>(json);
    

This creates a new instance of `MyClass` and sets the values on it using the
JSON data. If the JSON data contains values that do not map to fields in
`MyClass`, then the serializer ignores those values. If the JSON data is
missing values for fields in `MyClass`, then the serializer leaves the
constructed values for those fields in the returned object.

## Overwriting objects with JSON

You can also deserialize JSON data over an existing object, which overwrites
any existing data:

    
    
    JsonUtility.FromJsonOverwrite(json, myObject);
    

If the JSON data does not contain a value for a field, the serializer does not
change that field’s value. This method allows you to keep allocations to a
minimum by reusing objects that you created previously. It also allows you to
“patch” objects by deliberately overwriting them with JSON that only contains
a small subset of fields.

**Warning:** The JSON Serializer API supports
[MonoBehaviour](../ScriptReference/MonoBehaviour.html) and
[ScriptableObject](../ScriptReference/ScriptableObject.html) subclasses as
well as plain structs and classes. However, when deserializing JSON into
subclasses of `MonoBehaviour` or `ScriptableObject`, you must use the
[FromJsonOverwrite](../ScriptReference/JsonUtility.FromJsonOverwrite.html)
method. If you try to use
[FromJson](../ScriptReference/JsonUtility.FromJson.html), Unity throws an
exception because this behavior is not supported.

## Supported types

The JSON Serializer API supports any `MonoBehaviour` subclass,
`ScriptableObject` subclass, or plain class or struct with the
`[Serializable]` attribute. When you pass in an object to the standard Unity
serializer for processing, the same rules and limitations apply as they do in
the Inspector: Unity serializes fields only; and types like `Dictionary<>` are
not supported.

Unity does not support passing other types directly to the API, such as
primitive types or arrays. If you need to convert those, wrap them in a
`class` or `struct` of some sort.

In the Editor only, there is a parallel API,
[EditorJsonUtility](../ScriptReference/EditorJsonUtility.html), which allows
you to serialize any object derived from
[UnityEngine.Object](../ScriptReference/Object.html) both to and from JSON.
This produces JSON that contains the same data as the YAML representation of
the object.

[JsonUtility](../ScriptReference/JsonUtility.html) and
[EditorJsonUtility](../ScriptReference/EditorJsonUtility.html) are utility
classes for serializing Objects to and from JSON’s string format using [Unity
serialization rules](script-serialization-rules.html). In cases where it’s
necessary to manipulate JSON data through code, or to serialize data
structures that Unity’s serialization doesn’t support, you can use a general
purpose .NET JSON library as a companion to the JsonUtility API.

## Performance

Benchmark tests indicate that
[JsonUtility](../ScriptReference/JsonUtility.html) is significantly faster
than popular .NET JSON solutions, even though this class provides fewer
features in some cases.

Memory usage for garbage collection (GC) is at a minimum:

  * [ToJson](../ScriptReference/JsonUtility.ToJson.html) allocates GC memory only for the returned string.
  * [FromJson](../ScriptReference/JsonUtility.FromJson.html) allocates GC memory only for the returned object, as well as any subobjects needed (for example, if you deserialize an object that contains an array, then Unity allocates GC memory for the array).
  * [FromJsonOverwrite](../ScriptReference/JsonUtility.FromJsonOverwrite.html) allocates GC memory only as necessary for written fields (for example, strings and arrays). This means that Unity does not allocate any GC memory at all if all the fields being overwritten by the JSON are value-typed.

You can use the JsonUtility API from a background thread. However, as with any
multithreaded code, be careful not to access or alter an object on one thread
while another thread is serializing or deserializing it.

## Controlling the output of ToJson()

The [ToJson](../ScriptReference/JsonUtility.ToJson.html) method supports
pretty-printing the JSON output. It is off by default but you can turn it on
by passing `true` as the second parameter.

You can omit fields from the output by using the `[NonSerialized]` attribute.

## Using FromJson() with unknown types

If you don’t know the type of an object ahead of time, deserialize the JSON
into a class or struct that contains “common” fields, and then use the values
of those fields to work out what actual type you want. Then deserialize a
second time into that type.

[](script-serialization-how-unity-uses.html)

How Unity uses serialization

[](script-serialization-errors.html)

Script serialization errors

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

