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

#  [Editor](Editor.html).OnPreviewGUI

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

## Declaration

public void OnPreviewGUI([Rect](Rect.html) r, [GUIStyle](GUIStyle.html)
background);

### Parameters

r | The rectangle in which to draw the preview.  
---|---  
background | Background image.  
  
### Description

Creates a custom preview for the preview area of the Inspector, the headers of
the primary Editor, and the object selector.  
  
You must implement [Editor.HasPreviewGUI](Editor.HasPreviewGUI.html) for this
method to be called.

If you implement
[OnInteractivePreviewGUI](Editor.OnInteractivePreviewGUI.html), then this
method is only called for non-interactive custom previews. The overidden
method should render a preview of the asset in the specified rectangle (r).
The default implementation is a no-op.  
  
**Note:** Inspector previews are limited to the primary Editor of persistent
objects, such as GameObjectInspector, MaterialEditor, and TextureInspector. A
component cannot have its own Inspector preview.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    [CreateAssetMenu]
    class MyObject : [ScriptableObject](ScriptableObject.html)
    {
        public string text;
    }  
      
    // Show a preview of the text saved in MyObject.
    [[CustomEditor](CustomEditor.html)(typeof(MyObject))]
    public class MyObjectEditor : [Editor](Editor.html)
    {
        public override bool HasPreviewGUI() => true;  
      
        public override void OnPreviewGUI([Rect](Rect.html) r, [GUIStyle](GUIStyle.html) background)
        {
            [GUI.Label](GUI.Label.html)(r, (target as MyObject).text);
        }
    }
    

Additional resources:
[OnInteractivePreviewGUI](Editor.OnInteractivePreviewGUI.html).

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

