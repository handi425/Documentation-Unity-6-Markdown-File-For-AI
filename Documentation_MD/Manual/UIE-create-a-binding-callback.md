[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-create-a-binding-callback.html)
  * [中文](/cn/current/Manual/UIE-create-a-binding-callback.html)
  * [日本語](/ja/current/Manual/UIE-create-a-binding-callback.html)
  * [한국어](/kr/current/Manual/UIE-create-a-binding-callback.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-create-a-binding-callback.html)
  * [中文](/cn/current/Manual/UIE-create-a-binding-callback.html)
  * [日本語](/ja/current/Manual/UIE-create-a-binding-callback.html)
  * [한국어](/kr/current/Manual/UIE-create-a-binding-callback.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Data binding](UIE-data-binding.html)
  * [SerializedObject data binding](UIE-editor-binding.html)
  * [Binding examples](UIE-binding-examples.html)
  * Receive callbacks when a bound property changes

[](UIE-bind-uxml-template.html)

Bind to a UXML template

[](UIE-create-a-binding-callback-any-properties.html)

Receive callbacks when any bound properties change

# Receive callbacks when a bound property changes

**Version** : 2021.3+

This example demonstrates how to receive callbacks when a bound serialized
property changes.

## Example overview

This example creates a custom Editor window with a TextField that binds to the
name of a **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in a **scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). If the name of the GameObject is
`GameObject`, the background color of the text field label changes to dark
red.

![](../uploads/Main/uie_bind_callback_a_property.png)

You can find the completed files for the example in this [GitHub
repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-
examples/tree/master/callback-SerializedProperty-changes).

## Prerequisites

This guide is for developers familiar with the Unity Editor, **UI**(User
Interface) Allows a user to interact with your application. Unity currently
supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit, and C# scripting. Before you
start, get familiar with the following:

  * [`TrackPropertyValue()`](../ScriptReference/UIElements.BindingExtensions.TrackPropertyValue.html)
  * [`Unbind()`](../ScriptReference/UIElements.BindingExtensions.Unbind.html)

## Create the binding to receive a callback

Create a C# script that:

  * Calls the `CheckName()` method whenever the value of a serialized property changes
  * Registers the method with the `TrackPropertyValue()` extension method
  * Calls `Unbind()` before calling the `TrackPropertyValue()` again on another property.

A `VisualElement` can only track one property at any given time.

  1. Create a project in Unity with any template.

  2. In your **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), create a folder named
`callback-SerializedProperty-changes` to store your files.

  3. In the **callback-SerializedProperty-change** folder, create a folder named `Editor`.

  4. In the **Editor** folder, create a C# script named `SimpleBindingPropertyTrackingExample.cs` and replace its contents with the following:
    
        using UnityEditor;
    using UnityEngine;
    using UnityEditor.UIElements;
    using UnityEngine.UIElements;
    
    namespace UIToolkitExamples
    {
        public class SimpleBindingPropertyTrackingExample : EditorWindow
        {
            TextField m_ObjectNameBinding;
    
            [MenuItem("Window/UIToolkitExamples/Simple Binding Property Tracking Example")]
            public static void ShowDefaultWindow()
            {
                var wnd = GetWindow<SimpleBindingPropertyTrackingExample>();
                wnd.titleContent = new GUIContent("Simple Binding Property Tracking");
            }
                
            public void CreateGUI()
            {
                m_ObjectNameBinding = new TextField("Object Name Binding");
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
    
                    // Note: the "name" property of a GameObject is actually named "m_Name" in serialization.
                    SerializedProperty property = so.FindProperty("m_Name");
                        
                    // Ensure to use Unbind() before tracking a new property
                    m_ObjectNameBinding.Unbind();
                    m_ObjectNameBinding.TrackPropertyValue(property, CheckName);
    
                    // Bind the property to the field directly
                    m_ObjectNameBinding.BindProperty(property);
    
                    CheckName(property);
                }
                else
                {
                    // Unbind any binding from the field
                    m_ObjectNameBinding.Unbind();
                }
            }
    
            void CheckName(SerializedProperty property)
            {
                if (property.stringValue == "GameObject")
                {
                    m_ObjectNameBinding.style.backgroundColor = Color.red * 0.5f;
                }
                else
                {
                    m_ObjectNameBinding.style.backgroundColor = StyleKeyword.Null;
                }
            }
        }
    }
    

## Test the binding

  1. In Unity, select **Window** > **UIToolkitExamples** > **Simple Binding Property Tracking Example**. A custom Editor window appears with a text field.
  2. Select any GameObject in your scene. The name of the GameObject appears in your Editor window’s text field.
  3. Change the name of the GameObject in the text field. If the name is `GameObject`, the background color of the label changes to dark red.

## Additional resources

  * [SerializedObject data binding](UIE-Binding.html)
  * [Bindable elements](UIE-bindable-elements.html)
  * [Binding data type conversion](UIE-binding-data-type-conversion.html)
  * [Implementation details](UIE-binding-implementation-details.html)
  * [Binding examples](UIE-binding-examples.html)

[](UIE-bind-uxml-template.html)

Bind to a UXML template

[](UIE-create-a-binding-callback-any-properties.html)

Receive callbacks when any bound properties change

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

