[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UI-system-compare.html)
  * [中文](/cn/current/Manual/UI-system-compare.html)
  * [日本語](/ja/current/Manual/UI-system-compare.html)
  * [한국어](/kr/current/Manual/UI-system-compare.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UI-system-compare.html)
  * [中文](/cn/current/Manual/UI-system-compare.html)
  * [日本語](/ja/current/Manual/UI-system-compare.html)
  * [한국어](/kr/current/Manual/UI-system-compare.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * Comparison of UI systems in Unity

[](UIToolkits.html)

User interface (UI)

[](UIElements.html)

UI Toolkit

# Comparison of UI systems in Unity

[UI Toolkit](UIElements.html) is intended to become the recommended **UI**
system for your new UI development projects. However, in the current release,
UI Toolkit does not have some features that [Unity UI
(uGUI)](com.unity.ugui.html) and [Immediate Mode GUI
(IMGUI)](GUIScriptingGuide.html) support. uGUI and IMGUI are more appropriate
for certain use cases, and are required to support legacy projects.

This page provides a high-level feature comparison of UI Toolkit, uGUI, and
IMGUI, and their respective approaches to UI design.

## General consideration

The following table lists the recommended and alternative system for runtime
and Editor:

**Unity 6** | **Recommendation** | **Alternative**  
---|---|---  
**Runtime** | Unity UI | UI Toolkit  
**Editor** | UI Toolkit | IMGUI  
  
## Roles and skill sets

Your team’s skill set and comfort level with different technologies is also an
important consideration.

The following table lists the recommended system for different roles:

**Roles** | **UI Toolkit** | **Unity UI  
(uGUI)** | **IMGUI** | **Skill sets**  
---|---|---|---|---  
**Programmer** | Yes | Yes | Yes | Programmers can use any game development tool or API.  
**Technical Artist** | Partial | Yes | No | Technical artists who are familiar with Unity’s GameObject-based tools and workflows are likely to be comfortable working with GameObjects, Components, and the Scene view.   
  
They might not be comfortable with UI Toolkit’s web-like approach or IMGUI’s
pure C# approach.  
**UI Designer** | Yes | Partial | No | UI designers who are familiar with UI creation tools are likely to be comfortable with UI Toolkit’s document-based approach and can use the [UI Builder](UIBuilder.html) to visually edit their UI.  
  
If they are not familiar with GameObject-based workflows, they might require
help from programmers or level designers.  
  
## Innovation and development

UI Toolkit is in active development and releases new features frequently. uGUI
and IMGUI are established and production-proven UI systems that are updated
infrequently.

uGUI and IMGUI might be better choices if you need features that are not yet
available in UI Toolkit, or you need to support or reuse older UI content.

## Runtime

UI Toolkit is an alternative to Unity UI if you create a screen overlay UI
that runs on a wide variety of screen resolutions. Consider UI Toolkit to do
the following:

  * Produce work with a significant amount of user interfaces
  * Require familiar authoring workflows for artists and designers
  * Seek textureless UI rendering capabilities

Unity UI is the recommended solution for the following:

  * UI positioned and lit in a 3D world
  * VFX with custom **shaders** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) and materials

  * Easy referencing from `MonoBehaviours`

### Use Cases

The following table lists the recommended system for major runtime use cases:

**Unity 6** | **Recommendation**  
---|---  
**Multi-resolution menus and HUD in intensive UI projects** | UI Toolkit  
**World space UI and**VR** Virtual Reality [More info](VROverview.html)  
See in [Glossary](Glossary.html#VR)** | Unity UI  
**UI that requires customized shaders and materials** | Unity UI  
  
### In details

The following table lists the recommended system for detailed runtime
features:

**Unity 6** | **UI Toolkit** | **Unity UI**  
---|---|---  
**WYSIWYG authoring** | Yes | Yes  
**Nesting reusable components** | Yes | Yes  
**Global style management** | Yes | No  
**Layout and Styling Debugger** | Yes | Yes  
****Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) integration** | Yes | Yes  
**Rich text tags** | Yes | Yes*  
**Scalable text** | Yes | Yes*  
**Font fallbacks** | Yes | Yes*  
**Adaptive layout** | Yes | Yes  
**[Input system](com.unity.inputsystem.html) support** | Yes | Yes  
**Serialized events** | No | Yes  
**[Visual Scripting](com.unity.visualscripting.html) support** | No | Yes  
**Compatible with[Rendering pipelines](render-pipelines.html)** | Yes | Yes  
**Screen-space (2D) rendering** | Yes | Yes  
**World-space (3D) rendering** | No | Yes  
**Custom materials and shaders** | No | Yes  
**[Sprites](sprite/sprite-landing.html) A 2D graphic objects. If you are used
to working in 3D, Sprites are essentially just standard textures but there are
special techniques for combining and managing sprite textures for efficiency
and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) / [Sprite atlas](sprite/atlas/atlas-
landing.html)A utility that packs several sprite textures tightly together
within a single texture known as an atlas. [More
info](sprite/atlas/v2/v2-landing.html)  
See in [Glossary](Glossary.html#SpriteAtlas) support** | Yes | Yes  
**Dynamic texture atlas** | Yes | No  
**Textureless elements** | Yes | No  
**UI anti-aliasing** | Yes | No  
**Rectangle clipping** | Yes | Yes  
**Mask clipping** | No | Yes  
**Nested masking** | Yes | Yes  
**[UI transition animations](UIE-Transitions.html)** | Yes | No  
**Integration with**Animation Clips** Animation data that can be used for
animated characters or simple animations. It is a simple “unit” piece of
motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More
info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) and Timeline** | No | Yes  
  
*_Requires[the TextMesh Pro package](https://learn.unity.com/tutorial/textmesh-pro-importing-the-package#)_

## Editor

UI Toolkit is recommended if you create complex editor tools. UI Toolkit is
also recommended for the following reasons:

  * Better reusability and decoupling
  * Visual tools for authoring UI
  * Better scalability for code maintenance and performance

IMGUI is an alternative to UI Toolkit for the following:

  * Unrestricted access to editor extensible capabilities
  * Light API to quickly render UI on screen

### Use Cases

The following table lists the recommended system for major Editor use cases:

**Unity 6** | **Recommendation**  
---|---  
**Complex editor tool** | UI Toolkit  
****Property drawers** A Unity feature that allows you to customize the look
of certain controls in the Inspector window by using attributes on your
scripts, or by controlling how a specific Serializable class should look [More
info](editor-PropertyDrawers.html)  
See in [Glossary](Glossary.html#PropertyDrawer)** | UI Toolkit  
**Collaboration with designers** | UI Toolkit  
  
### In details

The following table lists the recommended system for detailed Editor features:

**Unity 6** | **UI Toolkit** | **IMGUI**  
---|---|---  
**WYSIWYG authoring** | Yes | No  
**Nesting reusable components** | Yes | No  
**Global style management** | Yes | Yes  
**Layout and Styling Debugger** | Yes | No  
**Rich text tags** | Yes | Yes  
**Scalable text** | Yes | No  
**Font fallbacks** | Yes | Yes  
**Adaptive layout** | Yes | Yes  
**Default**Inspectors** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** | Yes | Yes  
**Inspector: Edit custom object types** | Yes | Yes  
**Inspector: Edit custom property types** | Yes | Yes  
**Inspector: Mixed values (multi-editing) support** | Yes | Yes  
**[Array and list-view control](UIE-uxml-element-ListView.html)** | Yes | Yes  
**[Data binding: Serialized properties](UIE-Binding.html)** | Yes | Yes  
  
## Additional resources

  * [Migrate from Unity UI (UGUI) to UI Toolkit](UIE-Transitioning-From-UGUI.html)
  * [Migrate from Immediate Mode GUI (IMGUI) to UI Toolkit](UIE-IMGUI-migration.html)

[](UIToolkits.html)

User interface (UI)

[](UIElements.html)

UI Toolkit

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

