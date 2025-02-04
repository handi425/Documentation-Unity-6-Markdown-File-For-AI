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

#  [Editor](Editor.html).OnInteractivePreviewGUI

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

public void OnInteractivePreviewGUI([Rect](Rect.html) r,
[GUIStyle](GUIStyle.html) background);

### Parameters

r | Rectangle in which to draw the preview.  
---|---  
background | Background image.  
  
### Description

Implement to create your own interactive custom preview. Interactive custom
previews are used in the preview area of the inspector and the object
selector.

Implement this method, instead of [OnPreviewGUI](Editor.OnPreviewGUI.html), to
display interactive custom previews. You can implement both methods when some
previews are interactive and others are not. The overidden method should use
the rectangle passed in and render a preview of the asset. The default
implementation is a no-op.  
  
**Note:** Inspector previews are limited to the primary editor of persistent
objects (assets). For example, GameObjectInspector, MaterialEditor,
TextureInspector, and so on. This means that it is currently not possible for
a component to have its own inspector preview.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // Create an editor window which can display a chosen [GameObject](GameObject.html).
    // Use OnInteractivePreviewGUI to display the [GameObject](GameObject.html) and
    // allow it to be interactive.  
      
    public class ExampleClass: [EditorWindow](EditorWindow.html)
    {
        [GameObject](GameObject.html) gameObject;
        [Editor](Editor.html) gameObjectEditor;  
      
        [[MenuItem](MenuItem.html)("Example/[GameObject](GameObject.html) [Editor](Editor.html)")]
        static void ShowWindow()
        {
            GetWindowWithRect<ExampleClass>(new [Rect](Rect.html)(0, 0, 256, 256));
        }  
      
        void OnGUI()
        {
            gameObject = ([GameObject](GameObject.html)) [EditorGUILayout.ObjectField](EditorGUILayout.ObjectField.html)(gameObject, typeof([GameObject](GameObject.html)), true);  
      
            [GUIStyle](GUIStyle.html) bgColor = new [GUIStyle](GUIStyle.html)();
            bgColor.normal.background = [EditorGUIUtility.whiteTexture](EditorGUIUtility-whiteTexture.html);  
      
            if (gameObject != null)
            {
                if (gameObjectEditor == null)
                    gameObjectEditor = [Editor.CreateEditor](Editor.CreateEditor.html)(gameObject);  
      
                gameObjectEditor.OnInteractivePreviewGUI([GUILayoutUtility.GetRect](GUILayoutUtility.GetRect.html)(256, 256), bgColor);
            }
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

