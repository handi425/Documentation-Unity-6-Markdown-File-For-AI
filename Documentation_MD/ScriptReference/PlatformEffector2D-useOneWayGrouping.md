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

#  [PlatformEffector2D](PlatformEffector2D.html).useOneWayGrouping

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

public bool useOneWayGrouping;

### Description

Ensures that all contacts controlled by the one-way behaviour act the same.

When using the [oneWay](PlatformEffector2D-oneWay.html) behaviour, each
individual collider that comes into contact with the
[PlatformEffector2D](PlatformEffector2D.html) is checked to see if it should
be disabled or not by comparing its collision normal to the
[surfaceArc](PlatformEffector2D-surfaceArc.html). Working on each individual
collider like this can cause problems on objects that are comprised of
multiple colliders.  
  
If an object is comprised of many colliders and one of them has a contact
disabled due to the one-way behaviour then it may be preferable to do the same
for all colliders on the same object should they come into contact with the
same [PlatformEffector2D](PlatformEffector2D.html). To do this, set the
[useOneWayGrouping](PlatformEffector2D-useOneWayGrouping.html) to true. When
you do this, all colliders essentially act as one, all following each other
with regards to the one-way behaviour.  
  
When the [useOneWayGrouping](PlatformEffector2D-useOneWayGrouping.html) is not
enabled, an object comprised of multiple colliders could end up in a situation
where it has one collider contact disabled by passing through the one-way
platform, but have others not able to pass through.  
  
Additional resources: [useOneWay](PlatformEffector2D-useOneWay.html).

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

