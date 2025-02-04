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

#  [EditorUtility](EditorUtility.html).DisplayCancelableProgressBar

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

public static bool DisplayCancelableProgressBar(string title, string info,
float progress);

### Description

Displays or updates a progress bar that has a cancel button.

The window title sets to `title` and the info sets to `info`. Set progress
should to a value between 0.0 and 1.0, where 0 indicates nothing is loaded and
1.0 indicates loading is complete.  
  
This is useful when you perform a long blocking operation in an Editor script,
and want to notify the user of progress. Use this method for long operations
that make the Editor non-responsive. For long operations that happen in the
background, use the [Progress](Progress.html) class instead.  
  
A return value of true indicates that the user pressed the **Cancel** button.
When the return value is true, you must stop the task that is in progress.
After you display the progress bar, use
[EditorUtility.ClearProgressBar](EditorUtility.ClearProgressBar.html) to clear
it.  
  
Additional resources:
[EditorUtility.DisplayProgressBar](EditorUtility.DisplayProgressBar.html),
[EditorUtility.ClearProgressBar](EditorUtility.ClearProgressBar.html), and
[Progress](Progress.html).  
  
![](../StaticFiles/ScriptRefImages/EditorUtilityDisplayCancelableProgressBar.png)  
_Cancelable progress bar in the Editor._

    
    
    using System.Threading;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    // Shows a cancellable progress bar for the specified number of seconds.
    public class EditorUtilityDisplayCancelableProgressBar : [EditorWindow](EditorWindow.html)
    {
        public float secs = 5f;
        [[MenuItem](MenuItem.html)("Examples/[Progress](Progress.html) Bar Usage")]
        static void Init()
        {
            var window = GetWindow(typeof(EditorUtilityDisplayCancelableProgressBar));
            window.Show();
        }  
      
        void OnGUI()
        {
            secs = [EditorGUILayout.Slider](EditorGUILayout.Slider.html)("[Time](Time.html) to wait:", secs, 1.0f, 20.0f);
            if ([GUILayout.Button](GUILayout.Button.html)("[Display](Display.html) bar"))
            {
                var step = 0.1f;
                for (float t = 0; t < secs; t += step)
                {
                    if ([EditorUtility.DisplayCancelableProgressBar](EditorUtility.DisplayCancelableProgressBar.html)("Cancelable", "Doing some work...", t / secs))
                        break;
                    // Normally, some computation happens here.
                    // This example uses Sleep.
                    Thread.Sleep((int)(step * 1000.0f));
                }
                [EditorUtility.ClearProgressBar](EditorUtility.ClearProgressBar.html)();
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

