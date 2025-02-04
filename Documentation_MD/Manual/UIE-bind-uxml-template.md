[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-bind-uxml-template.html)
  * [中文](/cn/current/Manual/UIE-bind-uxml-template.html)
  * [日本語](/ja/current/Manual/UIE-bind-uxml-template.html)
  * [한국어](/kr/current/Manual/UIE-bind-uxml-template.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-bind-uxml-template.html)
  * [中文](/cn/current/Manual/UIE-bind-uxml-template.html)
  * [日本語](/ja/current/Manual/UIE-bind-uxml-template.html)
  * [한국어](/kr/current/Manual/UIE-bind-uxml-template.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Data binding](UIE-data-binding.html)
  * [SerializedObject data binding](UIE-editor-binding.html)
  * [Binding examples](UIE-binding-examples.html)
  * Bind to a UXML template

[](UIE-bind-to-nested-properties.html)

Bind to nested properties

[](UIE-create-a-binding-callback.html)

Receive callbacks when a bound property changes

# Bind to a UXML template

**Version** : 2021.3+

This example demonstrates how to set binding paths with UXML templates.

## Example overview

This example creates an asset menu item. The menu creates a `GameSwitch` asset
with three template instances that bind to properties of the `GameSwitch`
object.

![A preview of the GameSwitch Inspector](../uploads/Main/uxml_template.png) A
preview of the GameSwitch Inspector

You can find the completed files that this example creates in this [GitHub
repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-
examples/tree/master/bind-uxml-template).

## Prerequisites

This guide is for developers familiar with the Unity Editor, **UI**(User
Interface) Allows a user to interact with your application. Unity currently
supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit, and C# scripting. Before you
start, get familiar with the following:

  * [UI Builder](UIBuilder.html)
  * [Visual Tree](UIE-VisualTree.html)An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](Glossary.html#Visualtree)

  * [UXML](UIE-UXML.html)
  * [USS](UIE-USS.html)

## Create the GameSwitch asset

Create **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) to define the `GameSwitch` struct and
a custom asset to hold properties of the `GameSwitch` struct.

  1. Create a project in Unity with any template.

  2. In your **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), create a folder named `bind-
uxml-template` to store all your files.

  3. Create a C# script named `GameSwitch.cs` and replace its content with the following:
    
        using System;
    
    [Serializable]
    public struct GameSwitch
    {
        public string name;
        public bool enabled;
    }
    

  4. Create a C# script named `GameSwitchesAsset.cs` and replace its contents with the following: 
    
        using UnityEngine;
    
    [CreateAssetMenu(menuName = "UIToolkitExamples/GameSwitches")]
    public class GameSwitchesAsset : ScriptableObject
    {
        public GameSwitch useLocalServer;
        public GameSwitch showDebugMenu;
        public GameSwitch showFPSCounter;
    
        // Use the Reset function to provide default values
        public void Reset()
        {
            useLocalServer = new GameSwitch() { name = "Use Local Server", enabled = false };
            showDebugMenu = new GameSwitch() { name = "Show Debug Menu", enabled = false };
            showFPSCounter = new GameSwitch() { name = "Show FPS Counter", enabled = true };
        }
    }
    

## Create the UXML template and files

Create a UXML template that you can use for each `GameSwitch` struct instance,
and a UXML file that uses the template.

  1. Create a UI Document named `game_switch.uxml` and replace its contents with the following:
    
        <UXML xmlns="UnityEngine.UIElements" xmlns:ue="UnityEditor.UIElements">
        <Box style="flex-direction: row;">
            <Toggle binding-path="enabled" />
            <TextField binding-path="name" readonly="true" style="flex-grow: 1;"/>
        </Box>
    </UXML>
    

  2. In the **bind-uxml-template** folder, create a folder named `Editor`.

  3. In the **Editor** folder, create a UI Document named `game_switches_editor.uxml` and replace its contents with the following: 
    
        <UXML xmlns="UnityEngine.UIElements" xmlns:ue="UnityEditor.UIElements">
        <Template name="switch" src="../game_switch.uxml"/>
        <Instance template="switch" binding-path="useLocalServer" />
        <Instance template="switch" binding-path="showDebugMenu" />
        <Instance template="switch" binding-path="showFPSCounter" />
    </UXML>
    

**Note** : This is the main UXML file for the custom Editor. Each property
binds to an instance of `game_switch.uxml` through the `binding-path`
attribute of `Instance` .

## Create the asset menu and the asset

Create a script to register a custom Editor for `GameSwitchesAsset`.

  1. Create a C# script named `GameSwitchesEditor.cs` and replace its content with the following:
    
        using UnityEditor;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    namespace UIToolkitExamples
    {
        [CustomEditor(typeof(GameSwitchesAsset))]
        public class GameSwitchesEditor : Editor
        {
            [SerializeField]
            VisualTreeAsset visualTreeAsset;
    
            public override VisualElement CreateInspectorGUI()
            {
                return visualTreeAsset.CloneTree();
            }
        }
    }
    

  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window of `GameSwitchesEditor.cs`,
assign the `game_switches_editor.uxml` file to the **Visual Tree Asset**
field.

## Test the binding

  1. In Unity, select **Assets** > **Create** > **UIToolkitExamples** > **GameSwitches** to create a new asset in your project’s `Assets` folder.
  2. Select the newly created asset. The Inspector shows toggles and text fields that bind to the `GameSwitchesAsset.useLocalServer`, `GameSwitchesAsset.showDebugMenu`, and `GameSwitchesAsset.showFPSCounter` properties.

## Additional resources

  * [SerializedObject data binding](UIE-Binding.html)
  * [Bindable elements](UIE-bindable-elements.html)
  * [Binding data type conversion](UIE-binding-data-type-conversion.html)
  * [Implementation details](UIE-binding-implementation-details.html)
  * [Binding examples](UIE-binding-examples.html)

[](UIE-bind-to-nested-properties.html)

Bind to nested properties

[](UIE-create-a-binding-callback.html)

Receive callbacks when a bound property changes

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

