[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/script-serialization-errors.html)
  * [中文](/cn/current/Manual/script-serialization-errors.html)
  * [日本語](/ja/current/Manual/script-serialization-errors.html)
  * [한국어](/kr/current/Manual/script-serialization-errors.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/script-serialization-errors.html)
  * [中文](/cn/current/Manual/script-serialization-errors.html)
  * [日本語](/ja/current/Manual/script-serialization-errors.html)
  * [한국어](/kr/current/Manual/script-serialization-errors.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script serialization](script-serialization.html)
  * Script serialization errors

[](json-serialization.html)

JSON Serialization

[](script-serialization-best-practices.html)

Serialization best practice

# Script serialization errors

In certain circumstances, script serialization can cause errors. Fixes for
some of these are listed below.

## Calling Unity Scripting API from constructor or field initializers

Calling scripting APIs such as
[GameObject.Find](../ScriptReference/GameObject.Find.html) inside a
[MonoBehaviour](../ScriptReference/MonoBehaviour.html) constructor or field
initializer triggers the error: “Find is not allowed to be called from a
MonoBehaviour constructor (or instance field initializer), call in in Awake or
Start instead.”

Fix this by making the call to the scripting API in
[MonoBehaviour.Start](../ScriptReference/MonoBehaviour.Start.html) instead of
in the constructor.

## Calling Unity scripting API during deserialization

Calling scripting APIs such as
[GameObject.Find](../ScriptReference/GameObject.Find.html) from within the
constructor of a class marked with `System.Serializable` triggers the error:
“Find is not allowed to be called during serialization, call it from Awake or
Start instead.”

To fix this, edit your code so that it doesn’t make any scripting API calls in
any constructors for serialized objects.

## Thread-safe Unity scripting API

The majority of the scripting API is affected by the restrictions listed
above. Only select parts of the Unity scripting API are exempt and may be
called from anywhere. These are:

  * [Debug.Log](../ScriptReference/Debug.Log.html)

  * [Mathf](../ScriptReference/Mathf.html) functions

  * Simple self-contained structs; for example math structs like [Vector3](../ScriptReference/Vector3.html) and [Quaternion](../ScriptReference/Quaternion.html)Unity’s standard way of representing rotations as data. When writing code that deals with rotations, you should usually use the Quaternion class and its methods. [More info](QuaternionAndEulerRotationsInUnity.html)  
See in [Glossary](Glossary.html#Quaternion)

To reduce the risk of errors during serialization, only call API methods that
are self-contained and do not need to get or set data in Unity itself. Only
call these if there is no alternative.  
  

## Additional resources

  * [Serialization rules](script-serialization-rules.html)
  * [How Unity uses serialization](script-serialization-how-unity-uses.html)
  * [JSONSerialization](json-serialization.html)
  * [Serialization best practices](script-serialization-best-practices.html)

[](json-serialization.html)

JSON Serialization

[](script-serialization-best-practices.html)

Serialization best practice

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

