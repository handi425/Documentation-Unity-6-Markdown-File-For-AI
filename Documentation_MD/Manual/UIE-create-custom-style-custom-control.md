[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-create-custom-style-custom-control.html)
  * [中文](/cn/current/Manual/UIE-create-custom-style-custom-control.html)
  * [日本語](/ja/current/Manual/UIE-create-custom-style-custom-control.html)
  * [한국어](/kr/current/Manual/UIE-create-custom-style-custom-control.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-create-custom-style-custom-control.html)
  * [中文](/cn/current/Manual/UIE-create-custom-style-custom-control.html)
  * [日本語](/ja/current/Manual/UIE-create-custom-style-custom-control.html)
  * [한국어](/kr/current/Manual/UIE-create-custom-style-custom-control.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Structure UI examples](UIE-uxml-examples.html)
  * Create a custom style for a custom control

[](UIE-create-bindable-custom-control.html)

Create a bindable custom control

[](UIE-create-drag-and-drop-list-treeview-between-windows.html)

Create a drag-and-drop list and tree views between windows

# Create a custom style for a custom control

**Version** : 2023.2+

This example demonstrates how to use custom USS variables in a custom control.

## Example overview

This example creates a custom control that reads two colors from USS and uses
them to generate a texture.

![](../uploads/Main/custom-uss-gradient.png)

You can find the completed files that this example creates in this [GitHub
repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-
examples/tree/2023.2/create-custom-style-custom-control).

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

## Create the custom control

Create a C# script to define the custom control and a USS file to define the
custom style.

  1. Create a Unity project with any template.
  2. Create a folder named `create-custom-style-custom-control` to store your files.
  3. In the `ExampleElementCustomStyle` folder, create a C# script named `ExampleElementCustomStyle.cs` and replace its contents with the following:

    
    
    using UnityEngine;
    using UnityEngine.UIElements;
    
    namespace UIToolkitExamples
    {
        [UxmlElement]
        public partial class ExampleElementCustomStyle : VisualElement
        {
            // Use CustomStyleProperty<T> to fetch custom style properties from USS
            static readonly CustomStyleProperty<Color> S_GradientFrom = new CustomStyleProperty<Color>("--gradient-from");
            static readonly CustomStyleProperty<Color> S_GradientTo = new CustomStyleProperty<Color>("--gradient-to");
    
            // Image child element and its texture
            Texture2D m_Texture2D;
            Image m_Image;
    
            public ExampleElementCustomStyle()
            {
                // Create an Image and a texture for it. Attach Image to self.
                m_Texture2D = new Texture2D(100, 100);
                m_Image = new Image();
                m_Image.image = m_Texture2D;
                Add(m_Image);
    
                RegisterCallback<CustomStyleResolvedEvent>(OnStylesResolved);
            }
    
            // When custom styles are known for this control, make a gradient from the colors.
            void OnStylesResolved(CustomStyleResolvedEvent evt)
            {
                Color from, to;
    
                if (evt.customStyle.TryGetValue(S_GradientFrom, out from)
                    && evt.customStyle.TryGetValue(S_GradientTo, out to))
                {
                    GenerateGradient(from, to);
                }
            }
    
            public void GenerateGradient(Color from, Color to)
            {
                for (int i = 0; i < m_Texture2D.width; ++i)
                {
                    Color color = Color.Lerp(from, to, i / (float)m_Texture2D.width);
                    for (int j = 0; j < m_Texture2D.height; ++j)
                    {
                        m_Texture2D.SetPixel(i, j, color);
                    }
                }
    
                m_Texture2D.Apply();
                m_Image.MarkDirtyRepaint();
            }
        }
    }
    

## Create the custom control and custom style

Create a USS file named `ExampleElementCustomStyle.uss` and replace its
contents with the following:

    
    
    ExampleElementCustomStyle {
        --gradient-from: red;
        --gradient-to: yellow;
    }
    

## Use the custom control in UI Document

Create a UI Document to use the custom control and apply the custom style to
the custom control.

  1. In the `ExampleElementCustomStyle` folder, create a UI Document named `ExampleElementCustomStyle.uxml`.
  2. Double-click `ExampleElementCustomStyle.uxml` to open it in the UI Builder.
  3. Select **Library** > **Project** > **UIToolkitExamples** , and drag **ExampleElementCustomStyle** to the Hierarchy window. A grey square appears in the Viewport window.
  4. Add the `ExampleElementCustomStyle.uss` file as an existing USS. This applies the custom USS variables to the square.

## Additional resources

  * [Create custom controls](UIE-create-custom-controls.html)
  * [BEM standard](http://getbem.com/)

[](UIE-create-bindable-custom-control.html)

Create a bindable custom control

[](UIE-create-drag-and-drop-list-treeview-between-windows.html)

Create a drag-and-drop list and tree views between windows

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

