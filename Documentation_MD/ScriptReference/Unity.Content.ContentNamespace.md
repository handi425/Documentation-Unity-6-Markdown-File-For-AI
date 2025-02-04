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

# ContentNamespace

struct in Unity.Content

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Provides functionality for grouping loaded Archive files into separate
namespaces.

You can use the
[ContentNamespace.Default](Unity.Content.ContentNamespace.Default.html)
namespace, or create your own custom namespace with
[ContentNamespace.GetOrCreateNamespace](Unity.Content.ContentNamespace.GetOrCreateNamespace.html).  
  
**Note:** A ContentNamespace name must contain only alphanumeric characters
and can't be longer than 16 characters.  
  
Additional resources:
[ArchiveFileInterface.MountAsync](Unity.IO.Archive.ArchiveFileInterface.MountAsync.html).

### Static Properties

[Default](Unity.Content.ContentNamespace.Default.html)| Default
ContentNamespace object.  
---|---  
  
### Properties

[IsValid](Unity.Content.ContentNamespace.IsValid.html)| Indicates whether the
ContentNamespace still exists.  
---|---  
  
### Public Methods

[Delete](Unity.Content.ContentNamespace.Delete.html)| Destroys the specified
ContentNamespace object.  
---|---  
[GetName](Unity.Content.ContentNamespace.GetName.html)| Retrieves the name of
the ContentNamespace.  
  
### Static Methods

[GetAll](Unity.Content.ContentNamespace.GetAll.html)| Retrieves all existing
ContentNamespace objects.  
---|---  
[GetOrCreateNamespace](Unity.Content.ContentNamespace.GetOrCreateNamespace.html)|
Retrieves or creates the ContentNamespace if it doesn't exist.  
  
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

