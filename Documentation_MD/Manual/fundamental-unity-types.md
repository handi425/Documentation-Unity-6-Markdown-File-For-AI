[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/fundamental-unity-types.html)
  * [中文](/cn/current/Manual/fundamental-unity-types.html)
  * [日本語](/ja/current/Manual/fundamental-unity-types.html)
  * [한국어](/kr/current/Manual/fundamental-unity-types.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/fundamental-unity-types.html)
  * [中文](/cn/current/Manual/fundamental-unity-types.html)
  * [日本語](/ja/current/Manual/fundamental-unity-types.html)
  * [한국어](/kr/current/Manual/fundamental-unity-types.html)

  * [Scripting](scripting.html)
  * [Get started with scripting](scripting-get-started.html)
  * Fundamental Unity types

[](inspecting-scripts.html)

Inspecting scripts

[](class-Object.html)

Object

# Fundamental Unity types

Unity has some fundamental built-in classes that are particularly important
for scripting. These are classes which your own custom types can inherit from
to integrate with Editor and Engine functionality. It’s helpful to understand
these types, their behavior, and why you should inherit from or use them.

For a complete reference of all the built-in classes and every member
available, refer to the [Script Reference](../ScriptReference/index.html).

**Topic** | **Description**  
---|---  
[Object](class-Object.html)The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#Object) |  `UnityEngine.Object` is the base class for all objects the Editor can reference from fields in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window.  
[GameObject](class-GameObject.html) | Use the GameObject class to create and modify the GameObjects in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).  
[MonoBehaviour](class-MonoBehaviour.html) | Inherit from `MonoBehaviour` to make your script a component and control the behaviour of GameObjects and make them responsive to events.  
[ScriptableObject](class-ScriptableObject.html) | Inherit from `ScriptableObject` to store data that’s independent of GameObjects.  
[Transform](scripting-transform.html) | Control a GameObject’s position, rotation and scale via script, plus its hierarchical relationship to parent and child GameObjects.  
  
## Additional resources

  * [Unity Scripting reference](../ScriptReference/index.html)

[](inspecting-scripts.html)

Inspecting scripts

[](class-Object.html)

Object

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

