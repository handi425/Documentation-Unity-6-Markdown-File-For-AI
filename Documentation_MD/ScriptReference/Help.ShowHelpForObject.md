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

#  [Help](Help.html).ShowHelpForObject

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

public static void ShowHelpForObject([Object](Object.html) obj);

### Description

Show help page for this object.

Additional resources: [Help.HasHelpForObject](Help.HasHelpForObject.html),
[Help.GetHelpURLForObject](Help.GetHelpURLForObject.html).  
  
![](../StaticFiles/ScriptRefImages/QuickHelper.png)  
_Editor Window that lets you load docs for any Selected GameObject._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // EditorScript that quickly searchs for a help page
    // of the selected Object.
    //
    // If there is no page found on the Manual it opens the Unity forum.  
      
    class QuickHelper : [EditorWindow](EditorWindow.html)
    {
        Object source;  
      
        [@[MenuItem](MenuItem.html)("Example/QuickHelper _h")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = [EditorWindow.GetWindowWithRect](EditorWindow.GetWindowWithRect.html)(typeof(QuickHelper), new [Rect](Rect.html)(0, 0, 165, 100));
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();
            source = [EditorGUILayout.ObjectField](EditorGUILayout.ObjectField.html)(source, typeof(Object));
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Search!"))
            {
                if (source == null)
                {
                    this.ShowNotification(new [GUIContent](GUIContent.html)("No object selected for searching"));
                }
                else
                {
                    if ([Help.HasHelpForObject](Help.HasHelpForObject.html)(source))
                    {
                        [Help.ShowHelpForObject](Help.ShowHelpForObject.html)(source);
                    }
                    else
                    {
                        [Help.BrowseURL](Help.BrowseURL.html)("http://forum.unity3d.com/search.php");
                    }
                }
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

