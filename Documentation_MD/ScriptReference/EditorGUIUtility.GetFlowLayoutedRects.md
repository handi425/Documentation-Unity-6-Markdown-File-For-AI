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

#  [EditorGUIUtility](EditorGUIUtility.html).GetFlowLayoutedRects

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

public static List<Rect> GetFlowLayoutedRects([Rect](Rect.html) rect,
[GUIStyle](GUIStyle.html) style, float horizontalSpacing, float
verticalSpacing, List<string> items);

### Parameters

rect | Area where to layout the items.  
---|---  
style | Style for the items.  
horizontalSpacing | Extra horizontal spacing between successive items.  
verticalSpacing | Extra vertical spacing between item rows.  
items | Strings to layout.  
  
### Returns

**List <Rect>** List of rectangles for the passed items.

### Description

Layout list of string items left to right, top to bottom in the given area.

![](../StaticFiles/ScriptRefImages/EditorGUIUtilityGetFlowLayoutedRects.png)  
_Example of buttons positioned with GetFlowLayoutedRects._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.Collections.Generic;  
      
    public class MyWindow : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Window/My Window")]
        static void OpenMyWindow()
        {
            [EditorWindow.GetWindow](EditorWindow.GetWindow.html)<MyWindow>(true);
        }  
      
        void OnGUI()
        {
            // area to layout our items in
            var rect = new [Rect](Rect.html)(10, 10, position.width - 20, position.height - 20);
            // items to layout
            var items = new List<string>
            {
                "One button", "Another button", "Yet another", "Hey there's more", "More!"
            };
            // get resulting rectangles of items
            var style = [EditorStyles.miniButton](EditorStyles-miniButton.html);
            var boxes = [EditorGUIUtility.GetFlowLayoutedRects](EditorGUIUtility.GetFlowLayoutedRects.html)(rect, style, 4, 4, items);
            // do actual UI for them
            for (var i = 0; i < boxes.Count; ++i)
            {
                [GUI.Button](GUI.Button.html)(boxes[i], items[i], style);
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

