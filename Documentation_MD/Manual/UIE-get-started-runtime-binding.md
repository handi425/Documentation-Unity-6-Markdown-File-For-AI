[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-get-started-runtime-binding.html)
  * [中文](/cn/current/Manual/UIE-get-started-runtime-binding.html)
  * [日本語](/ja/current/Manual/UIE-get-started-runtime-binding.html)
  * [한국어](/kr/current/Manual/UIE-get-started-runtime-binding.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-get-started-runtime-binding.html)
  * [中文](/cn/current/Manual/UIE-get-started-runtime-binding.html)
  * [日本語](/ja/current/Manual/UIE-get-started-runtime-binding.html)
  * [한국어](/kr/current/Manual/UIE-get-started-runtime-binding.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Data binding](UIE-data-binding.html)
  * [Runtime data binding](UIE-runtime-binding.html)
  * Get started with runtime binding

[](UIE-runtime-binding.html)

Runtime data binding

[](UIE-runtime-binding-types.html)

Create a runtime binding in C# scripts

# Get started with runtime binding

**Version** : 6000.0+

Want to learn how to create runtime data binding? Use this example to get
started. This example creates a data source asset and uses **UI**(User
Interface) Allows a user to interact with your application. Unity currently
supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder to bind the data source to a UI.

To set a runtime binding in UI Builder:

  1. [Define the data source](UIE-runtime-binding-define-data-source.html) and the data source path in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) panel of the UI control.

  2. Bind the properties of the UI control to the properties of the data source asset.
  3. Define the [binding mode](UIE-runtime-binding-mode-update.html) to configure how changes are replicated between the data source and the UI.
  4. Define the [update trigger](UIE-runtime-binding-mode-update.html) to configure when changes are replicated between the data source and the UI.

## Example overview

This example creates a data source asset that contains a string property, and
binds it to the Text property of a Label control in UI Builder. When you
change the string property in the data source asset, the text of the label
changes.

![Runtime binding example](../uploads/Main/uitk/runtime-binding-get-
started.png) Runtime binding example

You can find the completed files that this example creates in this [GitHub
repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-
examples/tree/2023/runtime-data-binding).

## Prerequisites

This guide is for developers familiar with the Unity Editor, UI Toolkit, and
C# scripting. Before you start, get familiar with the following:

  * [UI Builder](UIBuilder.html)
  * [UXML](UIE-UXML.html)

## Create a data source asset

Create a data source asset that contains the properties you want to bind to.
In this example, you create a `ScriptableObject` asset named `ExampleObject`
that contains a `string` property.

  1. Create a project in Unity with any template.
  2. In the `Assets` folder of your project, create a C# script named `ExampleObject.cs` with the following content:

    
    
    using Unity.Properties;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    #if UNITY_EDITOR
    using UnityEditor;
    #endif
    
    [CreateAssetMenu]
    public class ExampleObject : ScriptableObject
    {
        [Header("Simple binding")]
        public string simpleLabel = "Hello World!";
    }
    

## Create the example object asset

  1. From the menu, select **Assets** > **Create** > **Example Object**. This creates an asset in the `Assets` folder of your project.
  2. Rename the asset as `ExampleObject.asset`.

## Create the UI

Create a UI that binds to the data source asset you created in the previous
step. In this example, you create a UXML file that contains a Label.

  1. In the `Assets` folder of your project, create a UXML file named `ExampleObject.uxml`.
  2. Double-click the `ExampleObject.uxml` file to open it in UI Builder.
  3. In the Hierarchy panel, add a **Label** control.

## Bind a Label to the data source

Bind the UI to the data source asset you created in the previous step.

  1. In the Inspector panel of the **Label** , from the **Bindings** > **Data Source** > **Object** list, select **ExampleObject**.

  2. In the **Data Source Path** list, select **simpleLabel**.

![Set the VisualElement binding data source](../uploads/Main/uitk/runtime-
binding-set-data-source.png)

  3. Right-click the **Text** property and select **Add binding**.

![Add binding](../uploads/Main/uitk/rumtime-binding-add-binding.png)

  4. From the **Binding Mode** list, select **To Target**. This updates the UI when the data source changes.

  5. From the **Advanced Settings** > **Update Trigger** list, select **On Source Changed** , which is the default setting. This updates the UI when the data source changes.

![Set the binding mode and update trigger](../uploads/Main/uitk/runtime-
binding-set-binding-mode.png)

  6. Select **Add binding** to apply your changes.

  7. Save and close UI Builder. Your `ExampleObject.uxml` file looks like the following:

    
    
    <engine:UXML xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:engine="UnityEngine.UIElements" 
    xmlns:editor="UnityEditor.UIElements" noNamespaceSchemaLocation="../../UIElementsSchema/UIElements.xsd" editor-extension-mode="False">
        <engine:Label text="Label" data-source="ExampleObject.asset" data-source-path="simpleLabel">
            <Bindings>
                <engine:DataBinding property="text" binding-mode="ToTarget" />
            </Bindings>
        </engine:Label>
    </engine:UXML>
    

## Test the binding in UI Builder preview mode

Update the label text of the LabelText in the data source asset and check
changes replicated in the UI.

  1. In the `Assets` folder of your project, select `ExampleObject.asset`.
  2. In the Inspector window, in the **Simple Label** field, enter random text. The **Label** text, in the UI Builder **Viewport** The user’s visible area of an app on their screen.  
See in [Glossary](Glossary.html#Viewport), changes to the text you entered.

## Additional resources

  * [Bind to multiple properties with runtime binding](UIE-bind-to-multiple-properties-with-runtime-binding.html)
  * [Create a runtime binding type converter](UIE-create-runtime-binding-type-converter.html)
  * [Create runtime data binding](UIE-runtime-binding-types.html)
  * [Define a data source](UIE-runtime-binding-define-data-source.html)

[](UIE-runtime-binding.html)

Runtime data binding

[](UIE-runtime-binding-types.html)

Create a runtime binding in C# scripts

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

