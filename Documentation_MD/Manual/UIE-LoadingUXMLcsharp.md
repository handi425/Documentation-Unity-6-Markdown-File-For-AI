[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-LoadingUXMLcsharp.html)
  * [中文](/cn/current/Manual/UIE-LoadingUXMLcsharp.html)
  * [日本語](/ja/current/Manual/UIE-LoadingUXMLcsharp.html)
  * [한국어](/kr/current/Manual/UIE-LoadingUXMLcsharp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-LoadingUXMLcsharp.html)
  * [中文](/cn/current/Manual/UIE-LoadingUXMLcsharp.html)
  * [日本語](/ja/current/Manual/UIE-LoadingUXMLcsharp.html)
  * [한국어](/kr/current/Manual/UIE-LoadingUXMLcsharp.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Structure UI with UXML](UIE-UXML.html)
  * Instantiate UXML from C# scripts

[](UIE-manage-asset-reference.html)

Load UXML and USS C# scripts

[](UIE-UQuery.html)

Find visual elements with UQuery

# Instantiate UXML from C# scripts

To build **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) from a UXML file, you must first [load the
file into a `VisualTreeAsset`](UIE-manage-asset-reference.html), and then use
the
[`Instantiate()`](../ScriptReference/UIElements.VisualTreeAsset.Instantiate.html)
to instantiate without a parent, which creates a new `TemplateContainer`, or
[`CloneTree(parent)`](../ScriptReference/UIElements.VisualTreeAsset.CloneTree.html))
to clone inside a parent.

Once the UXML is instantiated, you can retrieve specific elements from the
**visual tree** An object graph, made of lightweight nodes, that holds all the
elements in a window or panel. It defines every UI you build with the UI
Toolkit.  
See in [Glossary](Glossary.html#Visualtree) with [UQuery](UIE-UQuery.html).

The following example creates a custom Editor window and loads a UXML file as
its content:

    
    
    using UnityEditor;
    using UnityEngine;
    using UnityEngine.UIElements;
    using UnityEditor.UIElements;
    
    public class MyWindow : EditorWindow  {
        [MenuItem ("Window/My Window")]
        public static void  ShowWindow () {
            EditorWindow w = EditorWindow.GetWindow(typeof(MyWindow));
    
            VisualTreeAsset uiAsset = AssetDatabase.LoadAssetAtPath<VisualTreeAsset>("Assets/MyWindow.uxml");
            VisualElement ui = uiAsset.Instantiate();
    
            w.rootVisualElement.Add(ui);
        }
    }
    

## Additional resources

  * [Load UXML and USS from C# scripts](UIE-manage-asset-reference.html)
  * [UQuery](UIE-UQuery.html)

[](UIE-manage-asset-reference.html)

Load UXML and USS C# scripts

[](UIE-UQuery.html)

Find visual elements with UQuery

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

