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

#
[ProfilerModuleViewController](Unity.Profiling.Editor.ProfilerModuleViewController.html).Dispose(bool)

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

### Parameters

disposing | The flag to indicate whether the method call comes from a Dispose method or from a finalizer. A bool. When the value is true, the method call comes from a Dispose method. Otherwise, the method call comes from a finalizer.  
---|---  
  
### Description

Disposes the view controller. Unity calls this method automatically when the
view controller is no longer required, and its view will be removed from the
window hierarchy.

Override this method to do any necessary clean up of your view controller,
such as unsubscribing from events. You should always call the base
implementation afterwards. You do not need to explicitly remove the view
controller’s view from the hierarchy; Unity does this automatically when it
disposes of the view controller.  
  
For more information on the C# Dispose pattern, see Microsoft's documentation
on [Implementing dispose](https://docs.microsoft.com/en-
us/dotnet/standard/garbage-collection/implementing-dispose).

    
    
    protected override void Dispose(bool disposing)
    {
        if (disposing)
        {
            // Do any necessary clean up or freeing of managed resources.
        }  
      
        // Call the base implementation.
        base.Dispose(disposing);
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

