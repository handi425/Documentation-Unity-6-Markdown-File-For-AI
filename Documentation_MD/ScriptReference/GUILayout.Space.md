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

#  [GUILayout](GUILayout.html).Space

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

public static void Space(float pixels);

### Description

Insert a space in the current layout group.

The direction of the space is dependent on the layout group you're currently
in when issuing the command. If in a vertical group, the space will be
vertical. **Note:** This will override the
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html) and
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html)  
  
![](../StaticFiles/ScriptRefImages/GUILayoutSpace.png)  
_Space of 20px between two buttons._

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            [GUILayout.Button](GUILayout.Button.html)("I'm the first button");  
      
            // Insert 20 pixels of space between the 2 buttons.
            [GUILayout.Space](GUILayout.Space.html)(20);  
      
            [GUILayout.Button](GUILayout.Button.html)("I'm a bit further down");
        }
    }
    

In horizontal groups, the `pixels` are measured horizontally:

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            [GUILayout.BeginHorizontal](GUILayout.BeginHorizontal.html)();
            [GUILayout.Button](GUILayout.Button.html)("I'm the first button");  
      
            // Insert 20 pixels of space between the 2 buttons.
            [GUILayout.Space](GUILayout.Space.html)(20);  
      
            [GUILayout.Button](GUILayout.Button.html)("I'm the second button");
            [GUILayout.EndHorizontal](GUILayout.EndHorizontal.html)();
        }
    }
    

An example that is based on [EditorWindow](EditorWindow.html):

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // Example of using [GUILayout.Space](GUILayout.Space.html) inside an [EditorWindow](EditorWindow.html).
    // Clicking on the buttons changes the size of the [Space](Space.html).  
      
    public class ExampleClass : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/[GUILayout.Space](GUILayout.Space.html)")]
        static void CreateWindow()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow<ExampleClass>();
            window.Show();
        }  
      
        private float spaceSize = 20.0f;  
      
        void OnGUI()
        {
            if ([GUILayout.Button](GUILayout.Button.html)("Button1: Move Button2 down by 2 pixels"))
            {
                spaceSize = spaceSize + 2.0f;
            }  
      
            [GUILayout.Space](GUILayout.Space.html)(spaceSize);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Button2: Move up by 1 pixel"))
            {
                spaceSize = spaceSize - 1.0f;
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

