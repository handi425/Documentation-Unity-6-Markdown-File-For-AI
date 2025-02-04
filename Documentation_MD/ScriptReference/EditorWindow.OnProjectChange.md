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

#  [EditorWindow](EditorWindow.html).OnProjectChange()

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

### Description

Handler for message that is sent whenever the state of the project changes.

Actions that trigger this message include creating, renaming, or reparenting
assets, as well as moving or renaming folders in the project. Note that the
message is not sent immediately in response to these actions, but rather
during the next update of the editor application.  
  
Actions taken with assets that have
[HideFlags.HideInHierarchy](HideFlags.HideInHierarchy.html) set will not cause
this message to be sent.  
  
The [OnProjectChange](EditorWindow.OnProjectChange.html) message is used to
report when the items in the Project window change. Changes can include
examples such as new GameObjects or Materials being added to the project.
Additionally, adding folders with no contents will work as expected. As a
final example [OnProjectChange](EditorWindow.OnProjectChange.html) will be
used to see any changes in the Project window.  
Additional resources: [EditorApplication.projectChanged](EditorApplication-
projectChanged.html). .  

    
    
    using [UnityEditor](UnityEditor.html);  
      
    class MyEditor : [EditorWindow](EditorWindow.html)
    {
        void OnProjectChange()
        {
             // [Update](PlayerLoop.Update.html) editor according to changes in the Project
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

