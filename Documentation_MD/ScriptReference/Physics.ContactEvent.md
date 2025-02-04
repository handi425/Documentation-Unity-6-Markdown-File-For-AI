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

#  [Physics](Physics.html).ContactEvent

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

value | A delegate to call.  
---|---  
  
### Description

Subscribe to this event to read all collisions that occurred during the
physics simulation step.

Each subscriber to this event gets invoked with a physics scene and a native
array of [ContactPairHeader](ContactPairHeader.html)s. Each
[ContactPairHeader](ContactPairHeader.html) contains an array of
[ContactPair](ContactPair.html)s and each [ContactPair](ContactPair.html)
contains an array of [ContactPairPoint](ContactPairPoint.html)s.  
  
You can use this event to speed up contact processing as it's a lot faster
than [MonoBehaviour.OnCollisionEnter](MonoBehaviour.OnCollisionEnter.html) and
other messages. You can also use this event to schedule jobs that use the
provided native array. Jobs that are scheduled from this event must be
completed before the next [Physics.Simulate](Physics.Simulate.html),
[PhysicsScene.Simulate](PhysicsScene.Simulate.html), or
[PhysicsScene.RunSimulationStages](PhysicsScene.RunSimulationStages.html) with
the [RunSimulation](SimulationStage.RunSimulation.html) stage call. By default
a good place to complete these jobs is
[MonoBehaviour.FixedUpdate](MonoBehaviour.FixedUpdate.html).  
  
Notes:

  * Only Collider collisions are reported in this event and no trigger events will appear in the provided buffer.
  * All the data in the provided buffer is read-only. No writes are permited.
  * The event is invoked after the transform sync.
  * To receive contacts from a Collider, set the [Collider.providesContacts](Collider-providesContacts.html) property to `true` or attach a [MonoBehaviour](MonoBehaviour.html) script with an OnCollisionStay method.

    
    
    using System.Collections.Generic;
    using Unity.Collections;
    using Unity.Jobs;
    using UnityEngine;  
      
    public class BounceScipt : [MonoBehaviour](MonoBehaviour.html)
    {
        [[SerializeField](SerializeField.html)]
        private float m_ImpulseMultiplier = 5f;  
      
        private struct JobResultStruct
        {
            public int thisInstanceID;
            public int otherInstanceID;
            public [Vector3](Vector3.html) averageNormal;
        }  
      
        private NativeArray<JobResultStruct> m_ResultsArray;
        private int m_Count;
        private [JobHandle](Unity.Jobs.JobHandle.html) m_JobHandle;  
      
        private readonly Dictionary<int, [Rigidbody](Rigidbody.html)> m_RigidbodyMapping = new Dictionary<int, [Rigidbody](Rigidbody.html)>();  
      
        private void OnEnable()
        {
            m_ResultsArray = new NativeArray<JobResultStruct>(16, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));  
      
            [Physics.ContactEvent](Physics.ContactEvent.html) += Physics_ContactEvent;  
      
            var allRBs = GameObject.FindObjectsOfType<[Rigidbody](Rigidbody.html)>();
            foreach (var rb in allRBs)
                m_RigidbodyMapping.Add(rb.GetInstanceID(), rb);
        }  
      
        private void OnDisable()
        {
            m_JobHandle.Complete();
            m_ResultsArray.Dispose();  
      
            [Physics.ContactEvent](Physics.ContactEvent.html) -= Physics_ContactEvent;  
      
            m_RigidbodyMapping.Clear();
        }  
      
        private void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            m_JobHandle.Complete(); // The buffer is valid until the next [Physics.Simulate](Physics.Simulate.html)() call. Be it internal or manual  
      
            // Do something with the contact data.
            // E.g. Add force based on the average contact normal for that body
            for (int i = 0; i < m_Count; i++)
            {
                var thisInstanceID = m_ResultsArray[i].thisInstanceID;
                var otherInstanceID = m_ResultsArray[i].otherInstanceID;  
      
                var rb0 = thisInstanceID != 0 ? m_RigidbodyMapping[thisInstanceID] : null;
                var rb1 = otherInstanceID != 0 ? m_RigidbodyMapping[otherInstanceID] : null;  
      
                if (rb0)
                    rb0.AddForce(m_ResultsArray[i].averageNormal * m_ImpulseMultiplier, [ForceMode.Impulse](ForceMode.Impulse.html));
                if (rb1)
                    rb1.AddForce(m_ResultsArray[i].averageNormal * -m_ImpulseMultiplier, [ForceMode.Impulse](ForceMode.Impulse.html));
            }
        }  
      
        private void Physics_ContactEvent([PhysicsScene](PhysicsScene.html) scene, NativeArray<[ContactPairHeader](ContactPairHeader.html)>.[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html) pairHeaders)
        {
            int n = pairHeaders.Length;  
      
            if (m_ResultsArray.Length < n)
            {
                m_ResultsArray.Dispose();
                m_ResultsArray = new NativeArray<JobResultStruct>([Mathf.NextPowerOfTwo](Mathf.NextPowerOfTwo.html)(n), [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            }  
      
            m_Count = n;  
      
            AddForceJob job = new AddForceJob()
            {
                pairHeaders = pairHeaders,
                resultsArray = m_ResultsArray
            };  
      
            m_JobHandle = job.Schedule(n, 256);
        }  
      
        private struct AddForceJob : [IJobParallelFor](Unity.Jobs.IJobParallelFor.html)
        {
            [[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html)]
            public NativeArray<[ContactPairHeader](ContactPairHeader.html)>.[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html) pairHeaders;  
      
            public NativeArray<JobResultStruct> resultsArray;  
      
            public void Execute(int index)
            {
                [Vector3](Vector3.html) averageNormal = [Vector3.zero](Vector3-zero.html);
                int count = 0;  
      
                for (int j = 0; j < pairHeaders[index].pairCount; j++)
                {
                    ref readonly var pair = ref pairHeaders[index].GetContactPair(j);  
      
                    if (pair.IsCollisionExit)
                        continue;  
      
                    for (int k = 0; k < pair.ContactCount; k++)
                    {
                        ref readonly var contact = ref pair.GetContactPoint(k);
                        averageNormal += contact.Normal;
                    }  
      
                    count += pair.ContactCount;
                }  
      
                if (count != 0)
                    averageNormal /= (float)count;  
      
                JobResultStruct result = new JobResultStruct()
                {
                    thisInstanceID = pairHeaders[index].bodyInstanceID,
                    otherInstanceID = pairHeaders[index].otherBodyInstanceID,
                    averageNormal = averageNormal
                };  
      
                resultsArray[index] = result;
            }
        }
    }
    

This script reads all the contacts in the buffer and computes the average
normal for each ContactPairHeader. Then applies a force based on the result.

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

