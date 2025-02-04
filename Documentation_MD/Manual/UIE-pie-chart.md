[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-pie-chart.html)
  * [中文](/cn/current/Manual/UIE-pie-chart.html)
  * [日本語](/ja/current/Manual/UIE-pie-chart.html)
  * [한국어](/kr/current/Manual/UIE-pie-chart.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-pie-chart.html)
  * [中文](/cn/current/Manual/UIE-pie-chart.html)
  * [日本語](/ja/current/Manual/UIE-pie-chart.html)
  * [한국어](/kr/current/Manual/UIE-pie-chart.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [UI Renderer](UIE-ui-renderer.html)
  * Create a pie chart in the Editor and runtime UI

[](UIE-generate-2d-visual-content.html)

Generate 2D visual content

[](UIE-radial-progress-use-vector-api.html)

Use Vector API to create a radial progress indicator

# Create a pie chart in the Editor and runtime UI

**Version** : 2023.2+

This example demonstrates how to use the Vector API to create graphs in the
Editor and runtime **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI).

## Example overview

This example generates a pie chart onto a `VisualElement`, and displays it in
the Editor and runtime UI.

![A pie chart displays in a scene, and a pie chart displays in an Editor
window.](../uploads/Main/uitk/pie-chart.png) A pie chart displays in a scene,
and a pie chart displays in an Editor window.

You can find the completed files that this example creates in this [GitHub
repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-
examples/tree/2023.2/pie-chart).

## Prerequisites

This guide is for developers familiar with the Unity Editor, UI Toolkit, and
C# scripting. Before you start, get familiar with the following:

  * [Generate 2D visual content](UIE-generate-2d-visual-content.html)
  * [`MeshGenerationContext`](../ScriptReference/UIElements.MeshGenerationContext.html)

## Create the pie chart graph

Create a C# script that uses the
[`Arc`](../ScriptReference/UIElements.Painter2D.Arc.html) and
[`Fill`](../ScriptReference/UIElements.Painter2D.Fill.html) methods in the
Vector API to draw a pie chart into a **visual element** A node of a visual
tree that instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement).

  1. Create a Unity project with any template.
  2. Create a folder named `pie-chart` to store your files.
  3. In the `pie-chart` folder, create a C# script named `PieChart.cs` with the following content:

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    [UxmlElement]
    public partial class PieChart : VisualElement
    {
        float m_Radius = 100.0f;
        float m_Value = 40.0f;
    
        public float radius
        {
            get => m_Radius;
            set
            {
                m_Radius = value;
            }
        }
    
        public float diameter => m_Radius * 2.0f;
    
        public float value {
            get { return m_Value; }
            set { m_Value = value; MarkDirtyRepaint(); }
        }
    
        public PieChart()
        {
            generateVisualContent += DrawCanvas;
        }
    
        void DrawCanvas(MeshGenerationContext ctx)
        {
            var painter = ctx.painter2D;
            painter.strokeColor = Color.white;
            painter.fillColor = Color.white;
    
            var percentage = m_Value;
    
            var percentages = new float[] {
                percentage, 100 - percentage
            };
            var colors = new Color32[] {
                new Color32(182,235,122,255),
                new Color32(251,120,19,255)
            };
            float angle = 0.0f;
            float anglePct = 0.0f;
            int k = 0;
            foreach (var pct in percentages)
            {
                anglePct += 360.0f * (pct / 100);
    
                painter.fillColor = colors[k++];
                painter.BeginPath();
                painter.MoveTo(new Vector2(m_Radius, m_Radius));
                painter.Arc(new Vector2(m_Radius, m_Radius), m_Radius, angle, anglePct);
                painter.Fill();
    
                angle = anglePct;
            }
        }
    }
    

## Add the pie chart in the Editor UI

  1. Create a folder named `Editor` to store your files.
  2. In the `Editor` folder, create a C# script named `PieChartWindow.cs` with the following contents:

    
    
    using UnityEditor;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    public class PieChartWindow : EditorWindow
    {
        [MenuItem("Tools/PieChart Window")]
        public static void ShowExample()
        {
            PieChartWindow wnd = GetWindow<PieChartWindow>();
            wnd.titleContent = new GUIContent("PieChartWindow");
        }
    
        public void CreateGUI()
        {
            VisualElement root = rootVisualElement;
                
            root.Add(new PieChart());
        }
    }
    

To see the pie chart in the Editor window, from the menu, select **Tools** >
**PieChart Window**.

## Add the pie chart in the runtime UI

Add the pie chart in the UIDocument **GameObject** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in the SampleScene. To do so,
first, create a C# script named in the `pie-chart` folder`PieChartComponet.cs`
with the following content:

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    [RequireComponent(typeof(UIDocument))]
    public class PieChartComponent : MonoBehaviour
    {
        PieChart m_PieChart;
    
        void Start()
        {
            m_PieChart = new PieChart();
            GetComponent<UIDocument>().rootVisualElement.Add(m_PieChart);
        }
    }
    

To see the pie chart in runtime:

  1. In the SampleScene, select **GameObject** > **UI Toolkit** > **UI Document**.
  2. Select the **UIDocument** GameObject in the hierarchy.
  3. Add **PieChartComponet.cs** as a component of the UIDocument GameObject.
  4. Enter Play mode to see the pie chart in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

## Additional resources

  * [Use Vector API to create a radial progress](UIE-radial-progress-use-vector-api.html)

[](UIE-generate-2d-visual-content.html)

Generate 2D visual content

[](UIE-radial-progress-use-vector-api.html)

Use Vector API to create a radial progress indicator

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

