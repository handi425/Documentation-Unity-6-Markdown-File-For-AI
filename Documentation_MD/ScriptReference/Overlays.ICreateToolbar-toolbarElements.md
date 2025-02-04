[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [ICreateToolbar](Overlays.ICreateToolbar.html).toolbarElements

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

public IEnumerable<string> toolbarElements;

### Description

List of [toolbarElements](Overlays.ICreateToolbar-toolbarElements.html) IDs to
show when the [Overlay](Overlays.Overlay.html) is in a toolbar layout.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Overlays;
    using UnityEditor.Toolbars;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    [[Overlay](Overlays.Overlay.html)(typeof([SceneView](SceneView.html)), "My [Toolbar](UIElements.Toolbar.html) [Overlay](Overlays.Overlay.html)")]
    class MyOverlay : [Overlay](Overlays.Overlay.html), [ICreateToolbar](Overlays.ICreateToolbar.html)
    {
        public override [VisualElement](UIElements.VisualElement.html) CreatePanelContent()
        {
            return new [Label](UIElements.Label.html)("I'm the content shown in panel mode!");
        }
    
        public IEnumerable<string> toolbarElements
        {
            get
            {
                yield return MyToolbarItem.id;
                yield return SomeOtherToolbarItem.id;
            }
        }
    }
    
    [EditorToolbarElement(id, typeof([SceneView](SceneView.html)))]
    class SomeOtherToolbarItem : [EditorToolbarToggle](Toolbars.EditorToolbarToggle.html)
    {
        public const string id = "SomeOtherToolbarItem";
    
        public SomeOtherToolbarItem()
        {
            icon = [EditorGUIUtility.FindTexture](EditorGUIUtility.FindTexture.html)("CustomTool");
        }
    }
    
    // Example toolbar element with multiple controls
    [EditorToolbarElement(id, typeof([SceneView](SceneView.html)))]
    class MyToolbarItem : [OverlayToolbar](Overlays.OverlayToolbar.html)
    {
        public const string id = "MyToolbarItem";
    
        public MyToolbarItem()
        {
            var icon = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[Texture2D](Texture2D.html)>("MyIcon");
            Add(new [EditorToolbarButton](Toolbars.EditorToolbarButton.html)(icon, () => { [Debug.Log](Debug.Log.html)("Hello!"); }));
            Add(new [EditorToolbarButton](Toolbars.EditorToolbarButton.html)(icon, () => { [Debug.Log](Debug.Log.html)("Hello again!"); }));
            SetupChildrenAsButtonStrip();
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

