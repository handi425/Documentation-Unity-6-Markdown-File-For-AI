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

#  [GUI](GUI.html).depth

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

public static int depth;

### Description

The sorting depth of the currently executing GUI behaviour.

Set this to determine ordering when you have different scripts running
simultaneously. GUI elements drawn with lower depth values will appear on top
of elements with higher values (ie, you can think of the depth as "distance"
from the camera).  
  
**Note:** To see this example working, you will need to create 2 scripts.
Remember to name the scripts with the same name as the class names, else it
will not work.  
  
![](../StaticFiles/ScriptRefImages/GUIDepth.png)  
_One Button behind the other._

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Makes this button go back in depth  
      
    public class Example1 : [MonoBehaviour](MonoBehaviour.html)
    {
        public int guiDepth = 0;
        public Example2 example2;  
      
        private float buttonX, buttonY;  
      
        void Start()
        {
            buttonX = ([Screen.width](Screen-width.html) / 2) - 100;
            buttonY = ([Screen.height](Screen-height.html) / 2) - 100;
        }  
      
        void OnGUI()
        {
            [GUI.depth](GUI-depth.html) = guiDepth;
            [GUI.color](GUI-color.html) = [Color.yellow](Color-yellow.html);  
      
            [GUIStyle](GUIStyle.html) size = new [GUIStyle](GUIStyle.html)("button");
            size.fontSize = 16;  
      
            if ([GUI.RepeatButton](GUI.RepeatButton.html)(new [Rect](Rect.html)(buttonX, buttonY, 200, 100), "Go Backwards", size))
            {
                guiDepth = 1;
                example2.guiDepth = 0;
            }
        }
    }
    

And copy this other example to another script:

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Makes this button go back in depth  
      
    public class Example2 : [MonoBehaviour](MonoBehaviour.html)
    {
        public int guiDepth = 1;
        public Example1 example1;  
      
        private float buttonX, buttonY;  
      
        void Start()
        {
            buttonX = ([Screen.width](Screen-width.html) / 2)  - 50;
            buttonY = ([Screen.height](Screen-height.html) / 2) - 50;
        }  
      
        void OnGUI()
        {
            [GUI.depth](GUI-depth.html) = guiDepth;
            [GUI.color](GUI-color.html) = [Color.green](Color-green.html);  
      
            [GUIStyle](GUIStyle.html) size = new [GUIStyle](GUIStyle.html)("button");
            size.fontSize = 16;  
      
            if ([GUI.RepeatButton](GUI.RepeatButton.html)(new [Rect](Rect.html)(buttonX, buttonY, 200, 100), "Go Backwards", size))
            {
                guiDepth = 1;
                example1.guiDepth = 0;
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

