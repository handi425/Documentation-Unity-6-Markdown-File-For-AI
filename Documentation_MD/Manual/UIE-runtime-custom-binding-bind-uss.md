[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-runtime-custom-binding-bind-uss.html)
  * [中文](/cn/current/Manual/UIE-runtime-custom-binding-bind-uss.html)
  * [日本語](/ja/current/Manual/UIE-runtime-custom-binding-bind-uss.html)
  * [한국어](/kr/current/Manual/UIE-runtime-custom-binding-bind-uss.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-runtime-custom-binding-bind-uss.html)
  * [中文](/cn/current/Manual/UIE-runtime-custom-binding-bind-uss.html)
  * [日本語](/ja/current/Manual/UIE-runtime-custom-binding-bind-uss.html)
  * [한국어](/kr/current/Manual/UIE-runtime-custom-binding-bind-uss.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Data binding](UIE-data-binding.html)
  * [Runtime data binding](UIE-runtime-binding.html)
  * [Runtime data binding examples](UIE-runtime-binding-examples.html)
  * Create a custom binding to bind USS selectors

[](UIE-create-runtime-binding-type-converter.html)

Create a runtime binding with a type converter

[](UIE-runtime-binding-list-view.html)

Bind ListView to a list with runtime binding

# Create a custom binding to bind USS selectors

**Version** : 2023.2+

This example shows how to create a custom binding that binds USS selectors to
a **visual element** A node of a visual tree that instantiates or derives from
the C# [`VisualElement`](../ScriptReference/UIElements.VisualElement.html)
class. You can style the look, define the behaviour, and display it on screen
as part of the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement).

## Example overview

This example creates a custom binding that assigns USS class selectors to each
child element of a visual element based on the order of the child elements in
the hierarchy. The first element always has the left round corner edge, while
the last element always has the right round corner edge.

You can find the completed files that this example creates in this [GitHub
repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-
examples/tree/2023.2/runtime-custom-binding).

## Prerequisites

This guide is for developers familiar with the Unity Editor, **UI**(User
Interface) Allows a user to interact with your application. Unity currently
supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit, and C# scripting. Before you
start, get familiar with the following:

  * [UI Builder](UIBuilder.html)
  * [UXML](UIE-UXML.html)

## Create a custom binding type

Create a custom binding type that assigns USS classes based on the sibling
index. The binding updates only when the sibling index changes.

  1. Create a project in Unity with any template.

  2. In the `Assets` folder of your project, create a C# script named `AddMenuUSSClass.cs` with the following content:
    
        using UnityEngine.UIElements;
        
    [UxmlObject]
    public partial class AddMenuUssClass : CustomBinding
    {
        protected override BindingResult Update(in BindingContext context)
        {
            // Assign USS classes based on the sibling index. The binding updates when the sibling index changes.
            var element = context.targetElement;
            var index = element.parent.IndexOf(element);
            element.EnableInClassList("menu-button--first", index == 0);
            element.EnableInClassList("menu-button--last", index == element.parent.childCount - 1);                
                
            return new BindingResult(BindingStatus.Success);
        }
    }
    

## Create the UI and the binding

Generally speaking, you create a binding that binds to an existing property of
the element. For demonstration purposes, this example creates a custom binding
that binds to a property that doesn’t exist in the element. You must use UXML
or C# to set up the binding that binds to a non-existing property. This
example uses UXML to set up the binding.

  1. In the `Assets` folder of your project, create a USS file named `CustomBinding.uss` with the following contents:
    
        .menu-button {
        flex-direction: row;
        height: 64px;
        align-items: center; 
        justify-content: center;
    }
        
    .menu-button--first {
        border-top-left-radius: 15px;
        border-bottom-left-radius: 15px;
        border-left-width: 2px;
    }
        
    .menu-button--last {
        border-top-right-radius: 15px;
        border-bottom-right-radius: 15px;
        border-right-width: 2px;
    }
        
    Button {
        margin: 0px;
        border-color: red;
    }
    

  2. In the `Assets` folder of your project, create a UXML file named `CustomBinding.uxml` with the following contents:
    
        <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" editor-extension-mode="True">
        <ui:VisualElement class="menu-button">
            <ui:Button text="Bloub">
                <Bindings>
                    <AddMenuUssClass property="add-menu-button-class" />
                </Bindings>
            </ui:Button>
            <ui:Button text="Bip">
                <Bindings>
                    <AddMenuUssClass property="add-menu-button-class" />
                </Bindings>
            </ui:Button>
            <ui:Button text="Boop">
                <Bindings>
                    <AddMenuUssClass property="add-menu-button-class" />
                </Bindings>
            </ui:Button>
        </ui:VisualElement>
    </ui:UXML>
    

  3. Double-click the `CustomBinding.uxml` file to open it in UI Builder.

  4. In the StyleSheet panel, select **+** > **Add Existing USS** , and then select the `CustomBinding.uss` file.

  5. Save your changes. 

## Test the binding

To test the binding, change the order of the button elements in the UI Builder
and observe the changes in the UI Builder **Viewport** The user’s visible area
of an app on their screen.  
See in [Glossary](Glossary.html#Viewport).

  1. Double-click the `CustomBinding.uxml` file to open it in UI Builder.
  2. In the Hierarchy panel, expand the root VisualElement to display the child elements, which are buttons.
  3. Drag and drop the buttons to change their order. The first button always has the left round corner edge, while the last button always has the right round corner edge.

## Additional resources

  * [Runtime data binding](UIE-runtime-binding.html)
  * [Create runtime data binding](UIE-runtime-binding-types.html)
  * [Create custom binding types](UIE-runtime-binding-custom-types.html)

[](UIE-create-runtime-binding-type-converter.html)

Create a runtime binding with a type converter

[](UIE-runtime-binding-list-view.html)

Bind ListView to a list with runtime binding

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

