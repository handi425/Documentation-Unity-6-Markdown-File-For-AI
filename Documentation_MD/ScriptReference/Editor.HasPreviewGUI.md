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

#  [Editor](Editor.html).HasPreviewGUI

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

public bool HasPreviewGUI();

### Returns

**bool** True if this component can be Previewed in its current state.

### Description

Override this method in subclasses if you implement
[OnPreviewGUI](Editor.OnPreviewGUI.html).

You can also use it to disable or enable preview depending on the target
asset. The default implementation simply returns false, so if you override
[OnPreviewGUI](Editor.OnPreviewGUI.html) you have to override this method as
well.  
  
**Note:** Inspector previews are limited to the primary editor of persistent
objects (assets), e.g., GameObjectInspector, MaterialEditor, TextureInspector.
This means that it is currently not possible for a component to have its own
inspector preview.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class GameObjectEditorWindow: [EditorWindow](EditorWindow.html)
    {
        [GameObject](GameObject.html) gameObject;
        [Editor](Editor.html) gameObjectEditor;  
      
        [[MenuItem](MenuItem.html)("Window/[GameObject](GameObject.html) [Editor](Editor.html)")]
        static void ShowWindow()
        {
            GetWindow<GameObjectEditorWindow>("[GameObject](GameObject.html) [Editor](Editor.html)");
        }  
      
        void OnGUI()
        {
            gameObject = ([GameObject](GameObject.html)) [EditorGUILayout.ObjectField](EditorGUILayout.ObjectField.html)(gameObject, typeof([GameObject](GameObject.html)), true);  
      
            if (gameObject != null)
            {
                if (gameObjectEditor == null)
                    gameObjectEditor = [Editor.CreateEditor](Editor.CreateEditor.html)(gameObject);  
      
                gameObjectEditor.OnPreviewGUI([GUILayoutUtility.GetRect](GUILayoutUtility.GetRect.html)(500, 500), [EditorStyles.whiteLabel](EditorStyles-whiteLabel.html));
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

