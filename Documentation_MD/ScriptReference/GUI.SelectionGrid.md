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

#  [GUI](GUI.html).SelectionGrid

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

public static int SelectionGrid([Rect](Rect.html) position, int selected,
string[] texts, int xCount);

## Declaration

public static int SelectionGrid([Rect](Rect.html) position, int selected,
Texture[] images, int xCount);

## Declaration

public static int SelectionGrid([Rect](Rect.html) position, int selected,
GUIContent[] content, int xCount);

## Declaration

public static int SelectionGrid([Rect](Rect.html) position, int selected,
string[] texts, int xCount, [GUIStyle](GUIStyle.html) style);

## Declaration

public static int SelectionGrid([Rect](Rect.html) position, int selected,
Texture[] images, int xCount, [GUIStyle](GUIStyle.html) style);

## Declaration

public static int SelectionGrid([Rect](Rect.html) position, int selected,
GUIContent[] contents, int xCount, [GUIStyle](GUIStyle.html) style);

### Parameters

position | Rectangle on the screen to use for the grid.  
---|---  
selected | The index of the selected grid button.  
texts | An array of strings to show on the grid buttons.  
images | An array of textures on the grid buttons.  
contents | An array of text, image and tooltips for the grid button.  
xCount | How many elements to fit in the horizontal direction. The controls will be scaled to fit unless the style defines a fixedWidth to use.  
style | The style to use. If left out, the `button` style from the current [GUISkin](GUISkin.html) is used.  
  
### Returns

**int** The index of the selected button.

### Description

Make a grid of buttons.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public int selGridInt = 0;
        public string[] selStrings = new string[] {"[Grid](Grid.html) 1", "[Grid](Grid.html) 2", "[Grid](Grid.html) 3", "[Grid](Grid.html) 4"};  
      
        void OnGUI()
        {
            // use 2 elements in the horizontal direction
            selGridInt = [GUI.SelectionGrid](GUI.SelectionGrid.html)(new [Rect](Rect.html)(25, 25, 100, 30), selGridInt, selStrings, 2);
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

