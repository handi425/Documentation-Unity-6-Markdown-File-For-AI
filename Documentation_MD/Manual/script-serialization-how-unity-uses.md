[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/script-serialization-how-unity-uses.html)
  * [中文](/cn/current/Manual/script-serialization-how-unity-uses.html)
  * [日本語](/ja/current/Manual/script-serialization-how-unity-uses.html)
  * [한국어](/kr/current/Manual/script-serialization-how-unity-uses.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/script-serialization-how-unity-uses.html)
  * [中文](/cn/current/Manual/script-serialization-how-unity-uses.html)
  * [日本語](/ja/current/Manual/script-serialization-how-unity-uses.html)
  * [한국어](/kr/current/Manual/script-serialization-how-unity-uses.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script serialization](script-serialization.html)
  * How Unity uses serialization

[](script-serialization-custom-serialization.html)

Custom serialization

[](json-serialization.html)

JSON Serialization

# How Unity uses serialization

## Saving and loading

Unity uses serialization to load and save [scenes](CreatingScenes.html)A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), [Assets](AssetWorkflow.html)Any media
or data that can be used in your game or project. An asset may come from a
file created outside of Unity, such as a 3D Model, an audio file or an image.
You can also create some asset types in Unity, such as an Animator Controller,
an Audio Mixer or a Render Texture. [More info](AssetWorkflow.html)  
See in [Glossary](Glossary.html#Asset), and
[AssetBundles](AssetBundlesIntro.html) to and from your device’s memory. This
includes data saved in your own scripting API objects such as
[MonoBehaviour](../ScriptReference/MonoBehaviour.html) components and
[ScriptableObjects](class-ScriptableObject.html).

Many of the features in the Unity Editor are built on top of the core
serialization system. Two things to be particularly aware of with
serialization are the [Inspector window](UsingTheInspector.html), and hot
reloading.

### The Inspector window

The **Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window shows the value of the
serialized fields of the inspected objects. When you change a value in the
Inspector, the Inspector updates the serialized data and triggers a
deserialization that updates the inspected object.

The same applies for both built-in Unity objects, and scripting objects such
as MonoBehaviour-derived classes.

Unity doesn’t call any C# property getters and setters when you view or change
values in the Inspector window. Instead, Unity accesses the serialized backing
field directly.

### Hot reloading

Hot reloading of script code is performed as part of an asset database
refresh. It refers to the process of reloading and applying code changes
directly while the Editor is running, without having to restart it. For more
information, refer to [Refreshing the Asset
Database](AssetDatabaseRefreshing.html) and [Hot
reloading](AssetDatabaseRefreshing.html#hotreloading).

**Note** : Hot reloading is a special serialization case. Unlike in other
serialization cases, Unity serializes private fields by default when
reloading, even if they don’t have the
[SerializeField](../ScriptReference/Serializefield.html) attribute.

When Unity reloads **scripts** A piece of code that allows you to create your
own Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts):

  1. Unity serializes and stores all variables in all loaded scripts.
  2. Unity restores them to their original, pre-serialization values: 
     * Unity restores all variables - **including private variables** \- that fulfill the requirements for serialization, even if a variable has no `[SerializeField]` attribute. Sometimes, you need to prevent Unity from restoring private variables, for example, if you want a reference to be null after reloading from scripts. In this case, use the [`[field: NonSerialized]`](../ScriptReference/NonSerialized.html) attribute.
     * Unity never restores static variables, so don’t use static variables for states that you need to keep after Unity reloads a script because the reloading process will discard them.

## Prefabs

A [prefab](Prefabs.html)An asset type that allows you to store a GameObject
complete with components and properties. The prefab acts as a template from
which you can create new object instances in the scene. [More
info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) is the serialized data of one or more
[GameObjects](GameObjects.html)The fundamental object in Unity scenes, which
can represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) or [components](Components.html)A
functional part of a GameObject. A GameObject can contain any number of
components. Unity has many built-in components, and you can create your own by
writing scripts that inherit from MonoBehaviour. [More
info](UsingComponents.html)  
See in [Glossary](Glossary.html#component). A prefab instance contains a
reference to both the prefab source and a list of modifications to it. The
modifications are what Unity needs to do to the prefab source to create that
particular prefab instance.

The prefab instance only exists while you edit your project in the Unity
Editor. The Unity Editor instantiates a GameObject from its two sets of
serialization data: the prefab source and the prefab instance’s modifications.

## Instantiation

When you call [`Instantiate`](../ScriptReference/Object.Instantiate.html) on
anything that exists in a scene, such as a prefab or a GameObject:

  1. Unity serializes it. This happens both at runtime and in the Editor. Unity can serialize everything that derives from `UnityEngine.Object`.
  2. Unity creates a new GameObject and deserializes the data onto the new GameObject.
  3. Unity runs the same serialization code in a different variant to report which other `UnityEngine.Objects` it references. It checks all referenced `UnityEngine.Objects` to determine if they’re part of the data Unity instantiates. If the reference points to something external, such as a Texture, Unity keeps that reference as it is. If the reference points to something internal, such as a child GameObject, Unity patches the reference to the corresponding copy.

## Unloading unused assets

`EditorUtility.UnloadUnusedAssetsImmediate` is the native Unity garbage
collector and has a different purpose to the standard C# garbage collector. It
runs after you load a scene and checks for objects (like Textures) that it no
longer references and unloads them safely. The native Unity garbage collector
runs the serializer in a variation in which objects report all references to
external `UnityEngine.Objects`. This is how Textures that one scene uses, the
garbage collector unloads in the next.

## Differences between Editor and runtime serialization

Most serialization happens in the Editor, whereas deserialization is the focus
at runtime. Unity serializes some features only in the Editor, while it can
serialize other features in both the Editor and at runtime:

**Feature** | **Editor** | **Runtime**  
---|---|---  
**Assets in Binary Format** | Read/write supported | Read supported  
**Assets in YAML format** | Read/write supported | Not supported  
**Saving scenes, prefabs and other assets** | Supported, unless in Play mode | Not supported  
**Serialization of individual objects with[JsonUtility](json-serialization.html)** | Read/write support with JsonUtility.  
  
Support for additional types of objects with EditorJsonUtility | Read/write support with JsonUtility  
**[SerializeReference](../ScriptReference/SerializeReference.html)** | Supported | Supported  
**[ISerializationCallbackReceiver](../ScriptReference/ISerializationCallbackReceiver.html)** | Supported | Supported  
**[FormerlySerializedAs](../ScriptReference/Serialization.FormerlySerializedAsAttribute.html)** | Supported | Not supported  
  
Objects can have additional fields that only the Editor serializes, such as
when you declare fields within the UNITY_EDITOR [scripting symbol](platform-
dependent-compilation.html):

    
    
    public class SerializeRules : MonoBehaviour
    {
    #if UNITY_EDITOR
    public int m_intEditorOnly;
    #endif
    }
    

In the previous example, the `m_intEditorOnly` field is only serialized in the
editor and isn’t included in the build. This allows you to save memory by
omitting data that’s only required in the Editor from your build. Any code
that uses that field would also need to be conditionally compiled, for example
within `#if UNITY_EDITOR` blocks, so that the class can compile at build time.

The Editor doesn’t support objects with fields that Unity only serializes at
runtime, (for example, when you declare fields within the UNITY_STANDALONE
directive).

## Additional resources

  * [Serialization rules](script-serialization-rules.html)
  * [JSONSerialization](json-serialization.html)
  * [Serialization errors](script-serialization-errors.html)
  * [Serialization best practices](script-serialization-best-practices.html)

[](script-serialization-custom-serialization.html)

Custom serialization

[](json-serialization.html)

JSON Serialization

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

