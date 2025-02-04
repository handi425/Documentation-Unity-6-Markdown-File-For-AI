[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-Object.html)
  * [中文](/cn/current/Manual/class-Object.html)
  * [日本語](/ja/current/Manual/class-Object.html)
  * [한국어](/kr/current/Manual/class-Object.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-Object.html)
  * [中文](/cn/current/Manual/class-Object.html)
  * [日本語](/ja/current/Manual/class-Object.html)
  * [한국어](/kr/current/Manual/class-Object.html)

  * [Scripting](scripting.html)
  * [Get started with scripting](scripting-get-started.html)
  * [Fundamental Unity types](fundamental-unity-types.html)
  * Object

[](fundamental-unity-types.html)

Fundamental Unity types

[](class-GameObject.html)

GameObject

# Object

[Switch to Scripting](../ScriptReference/Object.html "Go to Object page in the
Scripting Reference")

The `UnityEngine.Object` class acts as a base class for all objects that Unity
can reference in the Unity Editor. You can drag and drop classes that inherit
from `UnityEngine.Object` into fields in the **Inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), or pick them using the Object
Picker next to an Object field.

![An example of an Object Field in the Inspector window. The Object Picker is
the circular icon to the right of the
field.](../uploads/Main/ExampleObjectField.png) An example of an Object Field
in the Inspector window. The Object Picker is the circular icon to the right
of the field.

Rather than inheriting directly from `Object` for your own custom classes,
it’s often better to inherit from a class designed to be more specific to your
goal. For example:

  * Inherit from `MonoBehaviour` if you want to write a custom component which you can add to a `GameObject`, to control what the `GameObject` does or provide some functionality relating to it.
  * Inherit from `ScriptableObject` if you want to create custom assets which can store serialized data.

Both of these inherit from `UnityEngine.Object` but provide extra
functionality to suit those purposes.

**Note:** `UnityEngine.Object` is different from .NET’s base `System.Object`,
which is not included in the default script template so that the names don’t
clash. You can still inherit from .NET’s `System.Object` if you want to create
classes which you don’t need to assign in the Inspector.

The `Object` class provides methods for instantiating and destroying Objects
and for finding references to Objects of a specific type. For more information
on the API for the Object class, refer to the [script reference page for
Object](../ScriptReference/Object.html).

## Special behavior of UnityEngine.Object

`UnityEngine.Object` is a special type of C# object in Unity, because it’s
linked to an unmanaged (C++) counterpart object. For example, when you use a
[Camera](../ScriptReference/Camera.html)A component which creates an image of
a particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) component, Unity stores the state of
the Object on the Object’s C++ counterpart, not on the C# Object itself.

![](../uploads/Main/unity-engine-object.png)

Unity doesn’t currently support the use of the C# `WeakReference` class with
instances of `UnityEngine.Object`. For this reason, you shouldn’t use a
`WeakReference` to reference a loaded asset. Refer to Microsoft’s
[WeakReference documentation](https://docs.microsoft.com/en-
us/dotnet/api/system.weakreference?view=netcore-3.1) for more information on
the `WeakReference` class.

### Unity C# and Unity C++ share UnityEngine Objects

When you use a method such as
[Object.Destroy](../ScriptReference/Object.Destroy.html) or
[Object.DestroyImmediate](../ScriptReference/Object.DestroyImmediate.html) to
destroy an object derived from `UnityEngine.Object`, Unity destroys (unloads)
the C++ counterpart object. You can’t destroy the C# object with an explicit
call, because the garbage collector manages the memory. Once there are no
longer any references to the managed object, the garbage collector collects
and destroys it.

If your application tries to access a destroyed `UnityEngine.Object` again,
Unity recreates the native counterpart object for most types. Two exceptions
to this recreation behavior are
[MonoBehaviours](../ScriptReference/MonoBehaviour.html) and
[ScriptableObjects](../ScriptReference/ScriptableObject.html): Unity never
reloads them once they have been destroyed.

`MonoBehaviour` and `ScriptableObject` override the equality (==) and
inequality (!=) operators. If you compare a destroyed `MonoBehaviour` or
`ScriptableObject` against `null`, the operators return true when the managed
object still exists and hasn’t yet been garbage collected.

Because you can’t overload the ?? and ?. operators, they aren’t compatible
with objects that derive from `UnityEngine.Object`. The operators don’t return
the same results as the equality and inequality operators when you use them on
a destroyed `MonoBehaviour` or `ScriptableObject` while the managed object
still exists.

## Additional resources

  * [Null references](null-reference-exception.html)
  * [UnityEngine.Object API reference](../ScriptReference/Object.html)

[](fundamental-unity-types.html)

Fundamental Unity types

[](class-GameObject.html)

GameObject

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

