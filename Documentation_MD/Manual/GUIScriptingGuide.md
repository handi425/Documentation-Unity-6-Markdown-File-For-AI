[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/GUIScriptingGuide.html)
  * [中文](/cn/current/Manual/GUIScriptingGuide.html)
  * [日本語](/ja/current/Manual/GUIScriptingGuide.html)
  * [한국어](/kr/current/Manual/GUIScriptingGuide.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/GUIScriptingGuide.html)
  * [中文](/cn/current/Manual/GUIScriptingGuide.html)
  * [日本語](/ja/current/Manual/GUIScriptingGuide.html)
  * [한국어](/kr/current/Manual/GUIScriptingGuide.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * Immediate Mode GUI (IMGUI)

[](com.unity.ugui.html)

Unity UI

[](gui-Basics.html)

IMGUI Basics

# Immediate Mode GUI (IMGUI)

The “Immediate Mode” GUI system (also known as IMGUI) is an entirely separate
feature to Unity’s main GameObject-based **UI**(User Interface) Allows a user
to interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) System. IMGUI is a code-driven GUI system,
and is mainly intended as a tool for programmers. It is driven by calls to the
****OnGUI**** function on any script which implements it. For example, this
code:

    
    
        void OnGUI() {
            if (GUILayout.Button("Press Me")){ 
                Debug.Log("Hello!");
            }
        }
    

Would result in a button displayed like so:

![The result of the above code
example](../uploads/Main/GUIScriptingGuideHelloExample.png) The result of the
above code example

The Immediate Mode GUI system is commonly used for:

  * Creating in-game debugging displays and tools.
  * Creating custom **inspectors** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) for script components.

  * Creating new editor windows and tools to extend Unity itself.

The IMGUI system is not generally intended to be used for normal in-game user
interfaces that players might use and interact with. For that you should use
Unity’s main GameObject-based [UI system](com.unity.ugui.html), which offers a
GameObject-based approach for editing and positioning UI elements, and has far
better tools to work with the visual design and layout of the UI.

“Immediate Mode” refers to the way the IMGUI is created and drawn. To create
IMGUI elements, you must write code that goes into a special function named
OnGUI. The code to display the interface is executed every frame, and drawn to
the screen. There are no persistent **gameobjects** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) other than the object to which
your OnGUI code is attached, or other types of objects in the hierarchy
related to the **visual elements** A node of a visual tree that instantiates
or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) that are drawn.

IMGUI allows you to create a wide variety of functional GUIs using code.
Rather than creating GameObjects, manually positioning them, and then writing
a script that handles its functionality, you can do everything at once with
just a few lines of code. The code produces **GUI controls** that are drawn
and handled with a single function call.

This section explains how to use IMGUI both in your game and in extensions to
the Unity editor.

[](com.unity.ugui.html)

Unity UI

[](gui-Basics.html)

IMGUI Basics

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

