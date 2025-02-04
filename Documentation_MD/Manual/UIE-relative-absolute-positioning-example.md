[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-relative-absolute-positioning-example.html)
  * [中文](/cn/current/Manual/UIE-relative-absolute-positioning-example.html)
  * [日本語](/ja/current/Manual/UIE-relative-absolute-positioning-example.html)
  * [한국어](/kr/current/Manual/UIE-relative-absolute-positioning-example.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-relative-absolute-positioning-example.html)
  * [中文](/cn/current/Manual/UIE-relative-absolute-positioning-example.html)
  * [日本語](/ja/current/Manual/UIE-relative-absolute-positioning-example.html)
  * [한국어](/kr/current/Manual/UIE-relative-absolute-positioning-example.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * [USS properties](UIE-uss-properties.html)
  * Relative and absolute positioning

[](UIE-LayoutEngine.html)

Position element with the layout engine

[](UIB-styling-ui-backgrounds.html)

Set background images

# Relative and absolute positioning

This example demonstrates the difference between relative and absolute
positioning. This example also demonstrates how to use C# and UXML/USS to add
and style **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) controls.

## Example overview

The example uses the automatic layout system to add boxes to an Editor and a
runtime UI. One box demonstrates a relative offset of `25 px`, while another
box demonstrates the absolute position of `25 px, 25 px`.

The example structures the Editor UI with C# script and the runtime UI with
UXML and CSS.

![Visual element positioning](../uploads/Main/UIEcoordinatesExample.png)
Visual element positioning

You can find the completed files that this example creates in this [GitHub
repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-
examples/tree/master/relative-and-absolute-position).

## Prerequisites

This guide is for developers familiar with the Unity Editor, UI Toolkit, and
C# scripting. Before you start, get familiar with the following:

  * [The visual tree](UIE-VisualTree.html)
  * [Coordinate and position systems](UIE-coordinate-and-position-system.html)
  * [UXML](UIE-UXML.html)
  * [USS](UIE-USS.html)

## Create the example for the Editor UI

Create a custom Editor window and add all the boxes with a C# script: four
boxes with gray backgrounds for comparison purposes; one box with a black
background set up using absolute position placement; one box with a purple
background set up using relative position placement.

  1. Create a Unity project with any template.

  2. Right-click in the Project window, then select **Create** > **UI Toolkit** > **Editor Window**.

  3. In the **C#** box of the **UI Toolkit Editor Window Creator** window, enter `PositioningTestWindow`.

  4. Clear the **UXML** and **USS** checkboxes.

  5. Select **Confirm**. This creates a C# file called `PositioningTestWindow.cs`.

  6. Replace `PositioningTestWindow.cs` with the following content:
    
        using UnityEditor;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    public class PositioningTestWindow : EditorWindow
    {
        [MenuItem("Window/UI Toolkit/Positioning Test Window")]
        public static void ShowExample()
        {
            var wnd = GetWindow<PositioningTestWindow>();
            wnd.titleContent = new GUIContent("Positioning Test Window");
        }
    
        public void CreateGUI()
        {
            for (int i = 0; i < 2; i++)
            {
                var temp = new VisualElement();
                temp.style.width = 70;
                temp.style.height = 70;
                temp.style.marginBottom = 2;
                temp.style.backgroundColor = Color.gray;
                this.rootVisualElement.Add(temp);
            }
    
            // Relative positioning
            var relative = new Label("Relative\nPos\n25, 0");
            relative.style.width = 70;
            relative.style.height = 70;
            relative.style.left = 25;
            relative.style.marginBottom = 2;
            relative.style.backgroundColor = new Color(0.2165094f, 0, 0.254717f);
            this.rootVisualElement.Add(relative);
    
            for (int i = 0; i < 2; i++)
            {
                var temp = new VisualElement();
                temp.style.width = 70;
                temp.style.height = 70;
                temp.style.marginBottom = 2;
                temp.style.backgroundColor = Color.gray;
                this.rootVisualElement.Add(temp);
            }
    
            // Absolute positioning
            var absolutePositionElement = new Label("Absolute\nPos\n25, 25");
            absolutePositionElement.style.position = Position.Absolute;
            absolutePositionElement.style.top = 25;
            absolutePositionElement.style.left = 25;
            absolutePositionElement.style.width = 70;
            absolutePositionElement.style.height = 70;
            absolutePositionElement.style.backgroundColor = Color.black;
            this.rootVisualElement.Add(absolutePositionElement);
        }
    }
    

  7. To see the example, from the menu, select **Window** > **UI Toolkit** > **Positioning Test Window**.

## Create the example for the runtime UI

  1. Create a USS file named `PositioningTest.uss` with the following content:
    
        .box {
        height: 70px;
        width: 70px;
        margin-bottom: 2px;
        background-color: gray;
    }
    #relative{
        width: 70px;
        height: 70px;
        background-color: purple;
        left: 25px;
        margin-bottom: 2px;
        position:relative;
    }
    #absolutePositionElement{
        left: 25px;
        top: 25px;
        width: 70px;
        height: 70px;
        background-color: black;
        position: absolute;
    }
    

  2. Create a UXML document named `PositioningTest.uxml` with the following content:
    
        <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements"
    xsi="http://www.w3.org/2001/XMLSchema-instance" engine="UnityEngine.UIElements"
    editor="UnityEditor.UIElements" noNamespaceSchemaLocation="../UIElementsSchema/UIElements.xsd"
    editor-extension-mode="False">
        <Style src="PositioningTest.uss"/>
        <ui:VisualElement class="box"/>
        <ui:VisualElement  class="box"/>
        <ui:Label text="Relative\nPos\n25, 0" name="relative" />
        <ui:VisualElement  class="box"/>
        <ui:VisualElement  class="box"/>
        <ui:Label text="Absolute\nPos\n25, 25" name="absolutePositionElement" />
    </ui:UXML>
    

  3. Create a C# script named `PositioningTestRuntime.cs` with the following content:
    
        using UnityEngine;
    using UnityEngine.UIElements;
    
    public class PostionTestRuntime : MonoBehaviour
    {
        void OnEnable()
        {
            GetComponent<UIDocument>();
        }
       }
    

  4. Right-click in the Hierarchy window, and then select **UI Toolkit** > **UI Document**.

  5. In the Inspector window of the **UI Document** , select **UI Document** > **Source Asset** > **PositioningTest**.

  6. In the Inspector window of the **UI Document** , select **Add Component** > **Positioning Test Runtime**.

  7. Enter Play mode and adjust the resolution as necessary to see the result.

## Additional resources

  * [Panels](UIE-panels.html)
  * [Draw order](UIE-draw-order.html)
  * [The Layout Engine](UIE-LayoutEngine.html)

[](UIE-LayoutEngine.html)

Position element with the layout engine

[](UIB-styling-ui-backgrounds.html)

Set background images

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

