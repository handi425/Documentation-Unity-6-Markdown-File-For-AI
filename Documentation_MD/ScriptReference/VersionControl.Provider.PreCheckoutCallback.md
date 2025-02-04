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

#  [Provider](VersionControl.Provider.html).PreCheckoutCallback

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
PreCheckoutCallback([VersionControl.AssetList](VersionControl.AssetList.html)
list, ref string changesetID, ref string changesetDescription);

### Parameters

list | The list of Assets that will be passed on to the Checkout command. Assets can be removed from or added to this list in the callback.  
---|---  
changesetID | Set this to the ID of an existing changeset to check out the listed Assets in that changeset. If no changeset matching the specified ID is found, the checkout will be blocked and an error message raised. Do not set both this and the changesetDescription parameter - this is not supported and an error will be raised.  
changesetDescription | To check the Assets out in a new changeset, set this description string. This action creates a new changeset, where the Assets open. Do not set both this description string and the changesetID parameter. Setting both causes an error.  
  
### Description

Delegate for a user-supplied callback to be called before Version Control
Checkout.

A PreCheckoutCallback may be set to enable the following: Permit the check out
by returning true from the callback. Prevent the check out by returning false
from the callback. Modify the list of Assets to be checked out (you may wish
to prevent certain Assets being checked out, or ensure that certain Assets are
checked out). Redirect the check out to an existing changeset. Create a new
changeset to check the Assets out in.  
  
Notes: The AssetList is absolute - Assets and/or their Meta Files will not be
automatically added after this callback returns. Setting both a changesetID
and a changesetDescription should ideally allow an existing changeset to be
renamed (to change its description) but this is not currently supported.
Attempting to set a changesetDescription when the VCS provider does not
support changesets will raise an error. Check for support by calling
[Provider.hasChangelistSupport](VersionControl.Provider-
hasChangelistSupport.html). You must not call any code inside this callback
that results in a further check out operation being created, as this will lead
to potentially infinite recursion. Be aware of Domain Reloads. If your
Assemblies are reloaded at any point then you need to set
[Provider.preCheckoutCallback](VersionControl.Provider-
preCheckoutCallback.html) again with your chosen callback.  
  
Additional resources: [Provider.preCheckoutCallback](VersionControl.Provider-
preCheckoutCallback.html),
[Provider.Checkout](VersionControl.Provider.Checkout.html),
[AssetDatabase.MakeEditable](AssetDatabase.MakeEditable.html).

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

