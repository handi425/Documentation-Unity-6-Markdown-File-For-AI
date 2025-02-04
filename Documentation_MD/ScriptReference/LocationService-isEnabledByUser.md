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

#  [LocationService](LocationService.html).isEnabledByUser

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

public bool isEnabledByUser;

### Description

Indicates whether the device allows the application to access the location
service.

Check this property before you start location updates to determine if the
device has location services enabled and that the application has access to
them.  
  
**Android** : The property returns false if the application has no permission
to access location. If you start the location service updates, the user
receives location permission request (unless already granted or permanently
denied). Before starting the location service updates, you can query to check
whether the application has location permission.  
  
**iOS** : The property returns false if the application has no permission to
access location. If you start the location updates anyway, the device prompts
the user with a confirmation panel asking whether to enable location services
for the application. For more information, refer to [Apple's developer
documentation](https://developer.apple.com/documentation/corelocation/cllocationmanager/locationservicesenabled\(\)?language=objc).  
  
**WebGL** : The property is false until you start location updates. Once
location updates start, it reflects the permissions granted by the user in the
browser.

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

