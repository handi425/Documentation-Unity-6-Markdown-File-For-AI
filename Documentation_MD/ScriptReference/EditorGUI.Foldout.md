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

#  [EditorGUI](EditorGUI.html).Foldout

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

public static bool Foldout([Rect](Rect.html) position, bool foldout, string
content, [GUIStyle](GUIStyle.html) style = EditorStyles.foldout);

## Declaration

public static bool Foldout([Rect](Rect.html) position, bool foldout, string
content, bool toggleOnLabelClick, [GUIStyle](GUIStyle.html) style =
EditorStyles.foldout);

## Declaration

public static bool Foldout([Rect](Rect.html) position, bool foldout,
[GUIContent](GUIContent.html) content, [GUIStyle](GUIStyle.html) style =
EditorStyles.foldout);

## Declaration

public static bool Foldout([Rect](Rect.html) position, bool foldout,
[GUIContent](GUIContent.html) content, bool toggleOnLabelClick,
[GUIStyle](GUIStyle.html) style = EditorStyles.foldout);

### Parameters

position | Rectangle on the screen to use for the arrow and label.  
---|---  
foldout | The shown foldout state.  
content | The label to show.  
style | Optional [GUIStyle](GUIStyle.html).  
toggleOnLabelClick | Should the label be a clickable part of the control?  
  
### Returns

**bool** The foldout state selected by the user. If true, you should render
sub-objects.

### Description

Makes a label with a foldout arrow to the left of it.

This is useful for creating tree or folder like structures where child objects
are only shown if the parent is folded out.  
  
![](../StaticFiles/ScriptRefImages/FoldoutUsageScreenshot.png)  
_Foldout in an Editor Window._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;  
      
    // Create a foldable menu that hides/shows the selected transform position.
    // if no [Transform](Transform.html) is selected, the [Foldout](UIElements.Foldout.html) item will be folded until a transform is selected.
    public class EditorGUIFoldout : [EditorWindow](EditorWindow.html)
    {
        public bool showPosition = true;
        public string status = "Select a [GameObject](GameObject.html)";
        [[MenuItem](MenuItem.html)("Examples/[Foldout](UIElements.Foldout.html) Usage")]
        static void Init()
        {
            UnityEditor.EditorWindow window = GetWindow(typeof(EditorGUIFoldout));
            window.position = new [Rect](Rect.html)(0, 0, 150, 60);
            window.Show();
        }  
      
        void OnGUI()
        {
            showPosition = [EditorGUI.Foldout](EditorGUI.Foldout.html)(new [Rect](Rect.html)(3, 3, position.width - 6, 15), showPosition, status);
            if (showPosition)
                if ([Selection.activeTransform](Selection-activeTransform.html))
                {
                    Selection.activeTransform.position = [EditorGUI.Vector3Field](EditorGUI.Vector3Field.html)(new [Rect](Rect.html)(3, 25, position.width - 6, 40), "[Position](UIElements.Position.html)", Selection.activeTransform.position);
                    status = Selection.activeTransform.name;
                }  
      
            if (![Selection.activeTransform](Selection-activeTransform.html))
            {
                status = "Select a [GameObject](GameObject.html)";
                showPosition = false;
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

