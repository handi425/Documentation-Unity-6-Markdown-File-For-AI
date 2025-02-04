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

#  [Progress](Progress.html).Start

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

public static int Start(string name, string description,
[Progress.Options](Progress.Options.html) options, int parentId);

### Parameters

name | The progress indicator's name. You can display the name as a title in the progress window. Use / (slash) as a separator to group child progress indicators together.  
---|---  
description | The progress indicator's initial description. You can change it using Report or SetDescription.  
parentId | The unique ID of the parent progress indicator, if any. If the progress indicator has no parent, pass -1.  
options | The progress indicator's initial progress options.  
  
### Returns

**int** The newly created progress identifier. This identifier is used for all
other APIs to update the progress status.

### Description

This method starts a new progress indicator.

    
    
    public IEnumerator Run_TwoTasks()
    {
        var title1 = "Running task 1...";
        var title2 = "Running task 2...";
        int progressId1 = [Progress.Start](Progress.Start.html)(title1);
        int progressId2 = [Progress.Start](Progress.Start.html)(title2);  
      
        [Progress.ShowDetails](Progress.ShowDetails.html)(false);
        yield return null;  
      
        for (int frame = 0; frame <= 10; ++frame)
        {
            [Progress.Report](Progress.Report.html)(progressId1, [Random.value](Random-value.html));
            yield return [WaitForSeconds](WaitForSeconds.html)(0.5f);
            [Progress.Report](Progress.Report.html)(progressId2, [Random.value](Random-value.html));
            yield return [WaitForSeconds](WaitForSeconds.html)(0.5f);
        }  
      
        [Progress.Remove](Progress.Remove.html)(progressId1);
        [Progress.Remove](Progress.Remove.html)(progressId2);
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

