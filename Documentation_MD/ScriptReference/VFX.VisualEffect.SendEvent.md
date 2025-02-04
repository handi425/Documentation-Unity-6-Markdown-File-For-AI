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

#  [VisualEffect](VFX.VisualEffect.html).SendEvent

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

public void SendEvent(int eventNameID);

## Declaration

public void SendEvent(string eventName);

## Declaration

public void SendEvent(int eventNameID,
[VFX.VFXEventAttribute](VFX.VFXEventAttribute.html) eventAttribute);

## Declaration

public void SendEvent(string eventName,
[VFX.VFXEventAttribute](VFX.VFXEventAttribute.html) eventAttribute);

### Parameters

eventName | The name of the event.  
---|---  
eventNameID | The ID of the event. This is the same ID that [Shader.PropertyToID](Shader.PropertyToID.html) returns.  
eventAttribute | Can be null or a VFXEventAttribute. To create a VFXEventAttribute, use [VisualEffect.CreateVFXEventAttribute](VFX.VisualEffect.CreateVFXEventAttribute.html).  
  
### Description

Use this method to send a custom named event.

    
    
    // The following example triggers the default visual effect play event once every second.
    using UnityEngine;
    using UnityEngine.VFX;
    public class SendEventExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [VisualEffect](VFX.VisualEffect.html) m_VisualEffect;
        private float m_Waiting = 1.0f;  
      
        private void [Update](PlayerLoop.Update.html)()
        {
            if (m_VisualEffect)
            {
                m_Waiting -= [Time.deltaTime](Time-deltaTime.html);
                if (m_Waiting < 0.0f)
                {
                    m_Waiting = 1.0f;
                    m_VisualEffect.SendEvent([VisualEffectAsset.PlayEventID](VFX.VisualEffectAsset.PlayEventID.html));
                }
            }
        }
    }
    
    
    
    // The following example triggers multiple events during the same frame every second.
    using UnityEngine;
    using UnityEngine.VFX;  
      
    public class SendEventExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [VisualEffect](VFX.VisualEffect.html) m_VisualEffect;
        private float m_Waiting = 1.0f;
        private int m_SpawnCountIdentifier;
        private int m_ColorIdentifier;
        private int m_EventNameIdentifier;  
      
        private void Start()
        {
            m_SpawnCountIdentifier = [Shader.PropertyToID](Shader.PropertyToID.html)("spawnCount");
            m_ColorIdentifier = [Shader.PropertyToID](Shader.PropertyToID.html)("color");
            m_EventNameIdentifier = [Shader.PropertyToID](Shader.PropertyToID.html)("direct");
        }  
      
        private void [Update](PlayerLoop.Update.html)()
        {
            if (m_VisualEffect)
            {
                m_Waiting -= [Time.deltaTime](Time-deltaTime.html);
                if (m_Waiting < 0.0f)
                {
                    m_Waiting = 1.0f;
                    var eventAttribute = m_VisualEffect.CreateVFXEventAttribute();
                    // Red
                    eventAttribute.SetFloat(m_SpawnCountIdentifier, 1);
                    eventAttribute.SetVector3(m_ColorIdentifier, new [Vector3](Vector3.html)(1, 0, 0));
                    m_VisualEffect.SendEvent(m_EventNameIdentifier, eventAttribute);
                    // Blue
                    eventAttribute.SetFloat(m_SpawnCountIdentifier, 3);
                    eventAttribute.SetVector3(m_ColorIdentifier, new [Vector3](Vector3.html)(0, 0, 1));
                    m_VisualEffect.SendEvent(m_EventNameIdentifier, eventAttribute);
                    // Green
                    eventAttribute.SetFloat(m_SpawnCountIdentifier, 2);
                    eventAttribute.SetVector3(m_ColorIdentifier, new [Vector3](Vector3.html)(0, 1, 0));
                    m_VisualEffect.SendEvent(m_EventNameIdentifier, eventAttribute);
                }
            }
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

