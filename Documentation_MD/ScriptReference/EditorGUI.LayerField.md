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

#  [EditorGUI](EditorGUI.html).LayerField

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

public static int LayerField([Rect](Rect.html) position, int layer,
[GUIStyle](GUIStyle.html) style = EditorStyles.popup);

## Declaration

public static int LayerField([Rect](Rect.html) position, string label, int
layer, [GUIStyle](GUIStyle.html) style = EditorStyles.popup);

## Declaration

public static int LayerField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, int layer, [GUIStyle](GUIStyle.html)
style = EditorStyles.popup);

### Parameters

position | Rectangle on the screen to use for the field.  
---|---  
label | Optional label in front of the field.  
layer | The layer shown in the field.  
style | Optional [GUIStyle](GUIStyle.html).  
  
### Returns

**int** The layer selected by the user.

### Description

Makes a layer selection field.

![](../StaticFiles/ScriptRefImages/EditorGUILayerField.png)  
_Layer field in an Editor Window._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    
    // Change the Tag and/or the layer of the selected GameObjects.  
      
    class EditorGUITagLayerField : [EditorWindow](EditorWindow.html)
    {
        string selectedTag = "";
        int selectedLayer = 0;  
      
        [[MenuItem](MenuItem.html)("Examples/Tag - [Layer](Experimental.GraphView.GraphView.Layer.html) for [Selection](Selection.html)")]
        static void Init()
        {
            var window = GetWindow<EditorGUITagLayerField>();
            window.position = new [Rect](Rect.html)(0, 0, 350, 70);
            window.Show();
        }  
      
        void OnGUI()
        {
            selectedTag = [EditorGUI.TagField](EditorGUI.TagField.html)(
                new [Rect](Rect.html)(3, 3, position.width / 2 - 6, 20),
                "New Tag:",
                selectedTag);  
      
            selectedLayer = [EditorGUI.LayerField](EditorGUI.LayerField.html)(
                new [Rect](Rect.html)(position.width / 2 + 3, 3, position.width / 2 - 6, 20),
                "New [Layer](Experimental.GraphView.GraphView.Layer.html):",
                selectedLayer);  
      
            if ([Selection.activeGameObject](Selection-activeGameObject.html))
            {
                if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(3, 25, 90, 17), "Change Tags"))
                {
                    foreach ([GameObject](GameObject.html) go in [Selection.gameObjects](Selection-gameObjects.html))
                    {
                        go.tag = selectedTag;
                    }
                }  
      
                if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(position.width - 96, 25, 90, 17), "Change Layers"))
                {
                    foreach ([GameObject](GameObject.html) go in [Selection.gameObjects](Selection-gameObjects.html))
                    {
                        go.layer = selectedLayer;
                    }
                }
            }
        }  
      
        void OnInspectorUpdate()
        {
            Repaint();
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

