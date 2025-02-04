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

#  [Provider](VersionControl.Provider.html).PreSubmitCallback

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

public delegate bool
PreSubmitCallback([VersionControl.AssetList](VersionControl.AssetList.html)
list, ref string changesetID, ref string changesetDescription);

### Parameters

list | The list of Assets that will be passed on to the Checkout command. Assets can be removed from or added to this list in the callback.  
---|---  
changesetID | Set this to the ID of an existing changeset to submit the listed Assets in that changeset. If no changeset matching the specified ID is found, the submission will be blocked and an error message raised.  
changesetDescription | If you wish to submit the Assets out in a new changeset, set this description string and a new changeset will be created and the Assets submitted there.  
  
### Description

Delegate for a user-supplied callback to be called before Version Control
Submit.

A PreSubmitCallback may be set to enable the following: Permit the submission
by returning true from the callback. Prevent the submission by returning false
from the callback. Modify the list of Assets to be submitted (you may wish to
prevent certain Assets being submitted, or ensure that certain Assets are
submitted). Redirect the submission to an existing changeset. Create a new
changeset to submit the Assets out in.  
  
Notes: The AssetList is absolute - Assets and/or their Meta Files will not be
automatically added after this callback returns but may be filtered out if
they are not in the correct state to be submitted. You must not call any code
inside this callback that results in a further submit operation being created,
as this will lead to potentially infinite recursion. Setting both changesetID
and changesetDescription will cause the changeset description of an existing
changeset to be changed during submission. Please be aware of Domain Reloads.
If your Assemblies are reloaded at any point then
[Provider.preSubmitCallback](VersionControl.Provider-preSubmitCallback.html)
will need to be set again with your chosen callback.

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

