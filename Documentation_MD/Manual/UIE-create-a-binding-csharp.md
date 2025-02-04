[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-create-a-binding-csharp.html)
  * [中文](/cn/current/Manual/UIE-create-a-binding-csharp.html)
  * [日本語](/ja/current/Manual/UIE-create-a-binding-csharp.html)
  * [한국어](/kr/current/Manual/UIE-create-a-binding-csharp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-create-a-binding-csharp.html)
  * [中文](/cn/current/Manual/UIE-create-a-binding-csharp.html)
  * [日本語](/ja/current/Manual/UIE-create-a-binding-csharp.html)
  * [한국어](/kr/current/Manual/UIE-create-a-binding-csharp.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Data binding](UIE-data-binding.html)
  * [SerializedObject data binding](UIE-editor-binding.html)
  * [Binding examples](UIE-binding-examples.html)
  * Bind with binding path in C# script

[](UIE-binding-examples.html)

Binding examples

[](UIE-bind-without-bindpath.html)

Bind without the binding path

# Bind with binding path in C# script

**Version** : 2021.3+

This example demonstrates how to bind with the binding path in a C# script.

## Example overview

This examples create a custom Editor window to change the name of a
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

![](../uploads/Main/uie_simple_binding.png)

You can find the completed files that this example creates in this [GitHub
repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-
examples/tree/master/bind-with-binding-path).

## Prerequisites

This guide is for developers familiar with the Unity Editor, **UI**(User
Interface) Allows a user to interact with your application. Unity currently
supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit, and C# scripting. Before you
start, get familiar with the following:

  * [`bindingPath`](../ScriptReference/UIElements.BindableElement-bindingPath.html)
  * [`Bind()`](../ScriptReference/UIElements.BindingExtensions.Bind.html)

## Bind with the binding path

Create a custom Editor window in C# with a `TextField`. Set the binding path
to the name property of a GameObject and make an explicit call to the `Bind()`
method.

  1. Create a project in Unity with any template.

  2. In your **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), create a folder named `bind-
with-binding-path` folder to store your file.

  3. In the **bind-with-binding-path** folder, create a folder named `Editor`.

  4. In the **Editor** folder, create a C# script named `SimpleBindingExample.cs` and replace its contents with the following:
    
        using UnityEditor;
    using UnityEngine;
    using UnityEditor.UIElements;
    using UnityEngine.UIElements;
    
    namespace UIToolkitExamples
    {
        public class SimpleBindingExample : EditorWindow
        {
            TextField m_ObjectNameBinding;
    
            [MenuItem("Window/UIToolkitExamples/Simple Binding Example")]
            public static void ShowDefaultWindow()
            {
                var wnd = GetWindow<SimpleBindingExample>();
                wnd.titleContent = new GUIContent("Simple Binding");
            }
    
            public void CreateGUI()
            {
                m_ObjectNameBinding = new TextField("Object Name Binding");
                // Note: the "name" property of a GameObject is "m_Name" in serialization.
                m_ObjectNameBinding.bindingPath = "m_Name";
                rootVisualElement.Add(m_ObjectNameBinding);
                OnSelectionChange();
            }
    
            public void OnSelectionChange()
            {
                GameObject selectedObject = Selection.activeObject as GameObject;
                if (selectedObject != null)
                {
                    // Create the SerializedObject from the current selection
                    SerializedObject so = new SerializedObject(selectedObject);
                    // Bind it to the root of the hierarchy. It will find the right object to bind to.
                    rootVisualElement.Bind(so);
    
                    // Alternatively you can instead bind it to the TextField itself.
                    // m_ObjectNameBinding.Bind(so);
                }
                else
                {
                    // Unbind the object from the actual visual element that was bound.
                    rootVisualElement.Unbind();
                    // If you bound the TextField itself, you'd do this instead:
                    // m_ObjectNameBinding.Unbind();
    
                    // Clear the TextField after the binding is removed
                    m_ObjectNameBinding.value = "";
                }
            }
        }
    }
    

## Test the binding

  1. In Unity, select **Window** > **UIToolkitExamples** > **Simple Binding Example**. A custom Editor window appears with a text field.
  2. Select any GameObject in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). The name of the GameObject appears in
your Editor window’s text field. If you change the name of the GameObject in
the text field, the name of the GameObject changes.

## Additional resources

  * [SerializedObject data binding](UIE-Binding.html)
  * [Bindable elements](UIE-bindable-elements.html)
  * [Binding data type conversion](UIE-binding-data-type-conversion.html)
  * [Implementation details](UIE-binding-implementation-details.html)
  * [Binding examples](UIE-binding-examples.html)

[](UIE-binding-examples.html)

Binding examples

[](UIE-bind-without-bindpath.html)

Bind without the binding path

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

