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

# ContextMenu Constructor

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

public ContextMenu(string itemName);

## Declaration

public ContextMenu(string itemName, bool isValidateFunction);

## Declaration

public ContextMenu(string itemName, bool isValidateFunction, int priority);

### Parameters

itemName | The name of the context menu item.  
---|---  
isValidateFunction | Whether this is a validate function (defaults to false).  
priority | Priority used to override the ordering of the menu items (defaults to 1000000). The lower the number the earlier in the menu it will appear.  
  
### Description

Adds the function to the context menu of the component.

In the inspector of the attached script. When the user selects the context
menu, the function will be executed.  
  
This is most useful for automatically setting up Scene data from the script.
The function has to be non-static.

    
    
    using UnityEngine;  
      
    public class ContextTesting : [MonoBehaviour](MonoBehaviour.html)
    {
        /// Add a context menu named "Do Something" in the inspector
        /// of the attached script.
        [[ContextMenu](ContextMenu.html)("Do Something")]
        void DoSomething()
        {
            [Debug.Log](Debug.Log.html)("Perform operation");
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

