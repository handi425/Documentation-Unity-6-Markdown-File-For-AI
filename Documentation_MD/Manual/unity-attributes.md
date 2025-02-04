[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/unity-attributes.html)
  * [中文](/cn/current/Manual/unity-attributes.html)
  * [日本語](/ja/current/Manual/unity-attributes.html)
  * [한국어](/kr/current/Manual/unity-attributes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/unity-attributes.html)
  * [中文](/cn/current/Manual/unity-attributes.html)
  * [日本語](/ja/current/Manual/unity-attributes.html)
  * [한국어](/kr/current/Manual/unity-attributes.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * Unity attributes

[](null-reference-exception.html)

Null references

[](compilation-and-code-reload.html)

Compilation and code reload

# Unity attributes

[Attributes](https://learn.microsoft.com/en-us/dotnet/csharp/advanced-
topics/reflection-and-attributes/) in C# are metadata markers that can be
placed above a class, property, or method declaration to indicate special
behaviour.

There are many attributes defined in the .NET libraries and Unity also
provides a number of custom, Unity-specific attributes. For example, you can
add the `HideInInspector` attribute above a property declaration to prevent
the **Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) from showing the property, even if
it is public. Attributes are specified in square brackets above the
declaration as follows:

    
    
    [HideInInspector]
    public float strength;
    

For the full list of `UnityEngine` attributes, refer to the list under
**UnityEngine > Attributes** in the Scripting API reference, which begins with
[AddComponentMenu](../ScriptReference/AddComponentMenu.html).

For the full list of `UnityEditor` attributes, refer to the list under
**UnityEditor > Attributes** in the Scripting API reference, which begins with
[AssetPostprocessorStaticVariableIgnoreAttribute](../ScriptReference/AssetPostprocessorStaticVariableIgnoreAttribute.html).

**Note:** Do not use the .NET [ThreadStatic](http://msdn.microsoft.com/en-
us/library/system.threadstaticattribute.aspx) attribute as this causes a crash
if you add it to a Unity script.

## Additional resources

  * [Unity Learn: attributes](https://learn.unity.com/tutorial/attributes#)
  * [Inspecting scripts](inspecting-scripts.html)
  * [Script serialization rules](script-serialization-rules.html)

[](null-reference-exception.html)

Null references

[](compilation-and-code-reload.html)

Compilation and code reload

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

