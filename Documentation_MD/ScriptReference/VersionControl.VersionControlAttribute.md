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

# VersionControlAttribute

class in UnityEditor.VersionControl

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

Allows you to mark a class as a version control system object.

This attribute enables Unity to detect custom VCS implementations. Your VCS
object must also derive from
[VersionControlObject](VersionControl.VersionControlObject.html).

    
    
    using UnityEditor.VersionControl;  
      
    [VersionControl("Custom")]
    public class CustomVersionControlObject : [VersionControlObject](VersionControl.VersionControlObject.html)
    {
    }
    

VCS object [name](VersionControl.VersionControlAttribute-name.html) must be
unique within Unity project.  
  
Additional resources:
[VersionControlObject](VersionControl.VersionControlObject.html),
[VersionControlManager](VersionControl.VersionControlManager.html),
[VersionControlDescriptor](VersionControl.VersionControlDescriptor.html).

### Properties

[displayName](VersionControl.VersionControlAttribute-displayName.html)|
Version control system display name.  
---|---  
[name](VersionControl.VersionControlAttribute-name.html)| Version control
system name.  
  
### Constructors

[VersionControlAttribute](VersionControl.VersionControlAttribute-ctor.html)|
Constructs VersionControlAttribute.  
---|---  
  
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

