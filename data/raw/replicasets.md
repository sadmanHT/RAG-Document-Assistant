ReplicaSet | Kubernetes
[Kubernetes](/)

* [Documentation](/docs/home/)
* [Kubernetes Blog](/blog/)
* [Training](/training/)
* [Careers](/careers/)
* [Partners](/partners/)
* [Community](/community/)
* [Versions](#)

  [Release Information](/releases)
  [v1.36](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
  [v1.35](https://v1-35.docs.kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
  [v1.34](https://v1-34.docs.kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
  [v1.33](https://v1-33.docs.kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
  [v1.32](https://v1-32.docs.kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
* [English](#)

  [中文 (Chinese)](/zh-cn/docs/concepts/workloads/controllers/replicaset/)
  [Français (French)](/fr/docs/concepts/workloads/controllers/replicaset/)
  [Deutsch (German)](/de/docs/concepts/workloads/controllers/replicaset/)
  [Bahasa Indonesia (Indonesian)](/id/docs/concepts/workloads/controllers/replicaset/)
  [日本語 (Japanese)](/ja/docs/concepts/workloads/controllers/replicaset/)
  [한국어 (Korean)](/ko/docs/concepts/workloads/controllers/replicaset/)
  [Português (Portuguese)](/pt-br/docs/concepts/workloads/controllers/replicaset/)
  [Español (Spanish)](/es/docs/concepts/workloads/controllers/replicaset/)
  [Tiếng Việt (Vietnamese)](/vi/docs/concepts/workloads/controllers/replicaset/)
  বাংলা (Bengali)
  [বাংলা (Bengali)](/bn/) 
  हिन्दी (Hindi)
  [हिन्दी (Hindi)](/hi/) 
  Italiano (Italian)
  [Italiano (Italian)](/it/) 
  Polski (Polish)
  [Polski (Polish)](/pl/) 
  Русский (Russian)
  [Русский (Russian)](/ru/) 
  Українська (Ukrainian)
  [Українська (Ukrainian)](/uk/)

# ReplicaSet

[English](#)

[বাংলা (Bengali)](/bn/docs/concepts/)
[中文 (Chinese)](/zh-cn/docs/concepts/)
[Français (French)](/fr/docs/concepts/)
[Deutsch (German)](/de/docs/concepts/)
[हिन्दी (Hindi)](/hi/docs/concepts/)
[Bahasa Indonesia (Indonesian)](/id/docs/concepts/)
[Italiano (Italian)](/it/docs/concepts/)
[日本語 (Japanese)](/ja/docs/concepts/)
[한국어 (Korean)](/ko/docs/concepts/)
[Polski (Polish)](/pl/docs/concepts/)
[Português (Portuguese)](/pt-br/docs/concepts/)
[Русский (Russian)](/ru/docs/concepts/)
[Español (Spanish)](/es/docs/concepts/)
[Українська (Ukrainian)](/uk/docs/concepts/)
[Tiếng Việt (Vietnamese)](/vi/docs/concepts/)

* [Kubernetes Documentation](/docs/ "Documentation")
  + [Documentation](/docs/home/ "Kubernetes Documentation")
    - [Available Documentation Versions](/docs/home/supported-doc-versions/)
  + [Getting started](/docs/setup/)
    - [Learning environment](/docs/setup/learning-environment/)
    - [Production environment](/docs/setup/production-environment/)
      * [Container Runtimes](/docs/setup/production-environment/container-runtimes/)
      * [Installing Kubernetes with deployment tools](/docs/setup/production-environment/tools/)
        + [Bootstrapping clusters with kubeadm](/docs/setup/production-environment/tools/kubeadm/)
          - [Installing kubeadm](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
          - [Troubleshooting kubeadm](/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/)
          - [Creating a cluster with kubeadm](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
          - [Customizing components with the kubeadm API](/docs/setup/production-environment/tools/kubeadm/control-plane-flags/)
          - [Options for Highly Available Topology](/docs/setup/production-environment/tools/kubeadm/ha-topology/)
          - [Creating Highly Available Clusters with kubeadm](/docs/setup/production-environment/tools/kubeadm/high-availability/)
          - [Set up a High Availability etcd Cluster with kubeadm](/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/)
          - [Configuring each kubelet in your cluster using kubeadm](/docs/setup/production-environment/tools/kubeadm/kubelet-integration/)
          - [Dual-stack support with kubeadm](/docs/setup/production-environment/tools/kubeadm/dual-stack-support/)
      * [Turnkey Cloud Solutions](/docs/setup/production-environment/turnkey-solutions/)
    - [Best practices](/docs/setup/best-practices/)
      * [Considerations for large clusters](/docs/setup/best-practices/cluster-large/)
      * [Running in multiple zones](/docs/setup/best-practices/multiple-zones/)
      * [Validate node setup](/docs/setup/best-practices/node-conformance/)
      * [Enforcing Pod Security Standards](/docs/setup/best-practices/enforcing-pod-security-standards/)
      * [PKI certificates and requirements](/docs/setup/best-practices/certificates/)
  + [Concepts](/docs/concepts/)
    - [Overview](/docs/concepts/overview/)
      * [Kubernetes Components](/docs/concepts/overview/components/)
      * [Objects In Kubernetes](/docs/concepts/overview/working-with-objects/)
        + [Kubernetes Object Management](/docs/concepts/overview/working-with-objects/object-management/)
        + [Object Names and IDs](/docs/concepts/overview/working-with-objects/names/)
        + [Labels and Selectors](/docs/concepts/overview/working-with-objects/labels/)
        + [Namespaces](/docs/concepts/overview/working-with-objects/namespaces/)
        + [Annotations](/docs/concepts/overview/working-with-objects/annotations/)
        + [Field Selectors](/docs/concepts/overview/working-with-objects/field-selectors/)
        + [Finalizers](/docs/concepts/overview/working-with-objects/finalizers/)
        + [Owners and Dependents](/docs/concepts/overview/working-with-objects/owners-dependents/)
        + [Recommended Labels](/docs/concepts/overview/working-with-objects/common-labels/)
        + [Storage Versions](/docs/concepts/overview/working-with-objects/storage-version/)
      * [The Kubernetes API](/docs/concepts/overview/kubernetes-api/)
      * [The kubectl command-line tool](/docs/concepts/overview/kubectl/)
    - [Cluster Architecture](/docs/concepts/architecture/)
      * [Nodes](/docs/concepts/architecture/nodes/)
      * [Communication between Nodes and the Control Plane](/docs/concepts/architecture/control-plane-node-communication/)
      * [Controllers](/docs/concepts/architecture/controller/)
      * [Leases](/docs/concepts/architecture/leases/)
      * [Cloud Controller Manager](/docs/concepts/architecture/cloud-controller/)
      * [About cgroup v2](/docs/concepts/architecture/cgroups/)
      * [Kubernetes Self-Healing](/docs/concepts/architecture/self-healing/)
      * [Garbage Collection](/docs/concepts/architecture/garbage-collection/)
      * [Mixed Version Proxy](/docs/concepts/architecture/mixed-version-proxy/)
    - [Containers](/docs/concepts/containers/)
      * [Images](/docs/concepts/containers/images/)
      * [Container Environment](/docs/concepts/containers/container-environment/)
      * [Runtime Class](/docs/concepts/containers/runtime-class/)
      * [Container Lifecycle Hooks](/docs/concepts/containers/container-lifecycle-hooks/)
      * [Container Runtime Interface (CRI)](/docs/concepts/containers/cri/)
    - [Workloads](/docs/concepts/workloads/)
      * [Pods](/docs/concepts/workloads/pods/)
        + [Pod Lifecycle](/docs/concepts/workloads/pods/pod-lifecycle/)
        + [Pod Conditions](/docs/concepts/workloads/pods/pod-condition/)
        + [Init Containers](/docs/concepts/workloads/pods/init-containers/)
        + [Sidecar Containers](/docs/concepts/workloads/pods/sidecar-containers/)
        + [Ephemeral Containers](/docs/concepts/workloads/pods/ephemeral-containers/)
        + [Disruptions](/docs/concepts/workloads/pods/disruptions/)
        + [Pod Hostname](/docs/concepts/workloads/pods/pod-hostname/)
        + [Pod Quality of Service Classes](/docs/concepts/workloads/pods/pod-qos/)
        + [Scheduling Group](/docs/concepts/workloads/pods/scheduling-group/)
        + [User Namespaces](/docs/concepts/workloads/pods/user-namespaces/)
        + [Downward API](/docs/concepts/workloads/pods/downward-api/)
        + [Advanced Pod Configuration](/docs/concepts/workloads/pods/advanced-pod-config/)
      * [Workload API](/docs/concepts/workloads/workload-api/)
        + [Pod Group Disruption and Priority](/docs/concepts/workloads/workload-api/disruption-and-priority/)
        + [PodGroup Scheduling Policies](/docs/concepts/workloads/workload-api/policies/)
        + [Topology-Aware Workload Scheduling](/docs/concepts/workloads/workload-api/topology-aware-scheduling/)
      * [Workload Management](/docs/concepts/workloads/controllers/)
        + [Deployments](/docs/concepts/workloads/controllers/deployment/)
        + [ReplicaSet](/docs/concepts/workloads/controllers/replicaset/)
        + [StatefulSets](/docs/concepts/workloads/controllers/statefulset/)
        + [DaemonSet](/docs/concepts/workloads/controllers/daemonset/)
        + [Jobs](/docs/concepts/workloads/controllers/job/)
        + [Automatic Cleanup for Finished Jobs](/docs/concepts/workloads/controllers/ttlafterfinished/)
        + [CronJob](/docs/concepts/workloads/controllers/cron-jobs/)
        + [ReplicationController](/docs/concepts/workloads/controllers/replicationcontroller/)
      * [PodGroup API](/docs/concepts/workloads/podgroup-api/)
        + [PodGroup Lifecycle](/docs/concepts/workloads/podgroup-api/lifecycle/)
      * [Managing Workloads](/docs/concepts/workloads/management/)
      * [Autoscaling Workloads](/docs/concepts/workloads/autoscaling/)
      * [Horizontal Pod Autoscaling](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
      * [Resource managers](/docs/concepts/workloads/resource-managers/)
      * [Vertical Pod Autoscaling](/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/)
    - [Services, Load Balancing, and Networking](/docs/concepts/services-networking/)
      * [Service](/docs/concepts/services-networking/service/)
      * [Ingress](/docs/concepts/services-networking/ingress/)
      * [Ingress Controllers](/docs/concepts/services-networking/ingress-controllers/)
      * [Gateway API](/docs/concepts/services-networking/gateway/)
      * [EndpointSlices](/docs/concepts/services-networking/endpoint-slices/)
      * [Network Policies](/docs/concepts/services-networking/network-policies/)
      * [DNS for Services and Pods](/docs/concepts/services-networking/dns-pod-service/)
      * [IPv4/IPv6 dual-stack](/docs/concepts/services-networking/dual-stack/)
      * [Topology Aware Routing](/docs/concepts/services-networking/topology-aware-routing/)
      * [Networking on Windows](/docs/concepts/services-networking/windows-networking/)
      * [Service ClusterIP allocation](/docs/concepts/services-networking/cluster-ip-allocation/)
      * [Service Internal Traffic Policy](/docs/concepts/services-networking/service-traffic-policy/)
    - [Storage](/docs/concepts/storage/)
      * [Volumes](/docs/concepts/storage/volumes/)
      * [Persistent Volumes](/docs/concepts/storage/persistent-volumes/)
      * [Projected Volumes](/docs/concepts/storage/projected-volumes/)
      * [Ephemeral Volumes](/docs/concepts/storage/ephemeral-volumes/)
      * [Storage Classes](/docs/concepts/storage/storage-classes/)
      * [Volume Attributes Classes](/docs/concepts/storage/volume-attributes-classes/)
      * [Dynamic Volume Provisioning](/docs/concepts/storage/dynamic-provisioning/)
      * [Volume Snapshots](/docs/concepts/storage/volume-snapshots/)
      * [Volume Snapshot Classes](/docs/concepts/storage/volume-snapshot-classes/)
      * [CSI Volume Cloning](/docs/concepts/storage/volume-pvc-datasource/)
      * [Storage Capacity](/docs/concepts/storage/storage-capacity/)
      * [Node-specific Volume Limits](/docs/concepts/storage/storage-limits/)
      * [Local ephemeral storage](/docs/concepts/storage/ephemeral-storage/)
      * [Volume Health Monitoring](/docs/concepts/storage/volume-health-monitoring/)
      * [Windows Storage](/docs/concepts/storage/windows-storage/)
    - [Configuration](/docs/concepts/configuration/)
      * [ConfigMaps](/docs/concepts/configuration/configmap/)
      * [Secrets](/docs/concepts/configuration/secret/)
      * [Liveness, Readiness, and Startup Probes](/docs/concepts/configuration/liveness-readiness-startup-probes/)
      * [Resource Management for Pods and Containers](/docs/concepts/configuration/manage-resources-containers/)
      * [Organizing Cluster Access Using kubeconfig Files](/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
      * [Resource Management for Windows nodes](/docs/concepts/configuration/windows-resource-management/)
    - [Security](/docs/concepts/security/)
      * [Cloud Native Security](/docs/concepts/security/cloud-native-security/ "Cloud Native Security and Kubernetes")
      * [Pod Security Standards](/docs/concepts/security/pod-security-standards/)
      * [Pod Security Admission](/docs/concepts/security/pod-security-admission/)
      * [Service Accounts](/docs/concepts/security/service-accounts/)
      * [Pod Security Policies](/docs/concepts/security/pod-security-policy/)
      * [Security For Linux Nodes](/docs/concepts/security/linux-security/)
      * [Security For Windows Nodes](/docs/concepts/security/windows-security/)
      * [Controlling Access to the Kubernetes API](/docs/concepts/security/controlling-access/)
      * [Role Based Access Control Good Practices](/docs/concepts/security/rbac-good-practices/)
      * [Good practices for Kubernetes Secrets](/docs/concepts/security/secrets-good-practices/)
      * [Multi-tenancy](/docs/concepts/security/multi-tenancy/)
      * [Hardening Guide - Authentication Mechanisms](/docs/concepts/security/hardening-guide/authentication-mechanisms/)
      * [Hardening Guide - Dynamic Resource Allocation](/docs/concepts/security/hardening-guide/dynamic-resource-allocation/)
      * [Hardening Guide - Scheduler Configuration](/docs/concepts/security/hardening-guide/scheduler/)
      * [Kubernetes API Server Bypass Risks](/docs/concepts/security/api-server-bypass-risks/)
      * [Linux kernel security constraints for Pods and containers](/docs/concepts/security/linux-kernel-security-constraints/)
      * [Security Checklist](/docs/concepts/security/security-checklist/)
      * [Application Security Checklist](/docs/concepts/security/application-security-checklist/)
    - [Policies](/docs/concepts/policy/)
      * [Limit Ranges](/docs/concepts/policy/limit-range/)
      * [Resource Quotas](/docs/concepts/policy/resource-quotas/)
      * [Process ID Limits And Reservations](/docs/concepts/policy/pid-limiting/)
    - [Scheduling, Preemption and Eviction](/docs/concepts/scheduling-eviction/)
      * [Kubernetes Scheduler](/docs/concepts/scheduling-eviction/kube-scheduler/)
      * [Topology-Aware Workload Scheduling](/docs/concepts/scheduling-eviction/topology-aware-scheduling/)
      * [Assigning Pods to Nodes](/docs/concepts/scheduling-eviction/assign-pod-node/)
      * [Pod Overhead](/docs/concepts/scheduling-eviction/pod-overhead/)
      * [Pod Scheduling Readiness](/docs/concepts/scheduling-eviction/pod-scheduling-readiness/)
      * [Pod Topology Spread Constraints](/docs/concepts/scheduling-eviction/topology-spread-constraints/)
      * [Taints and Tolerations](/docs/concepts/scheduling-eviction/taint-and-toleration/)
      * [Scheduling Framework](/docs/concepts/scheduling-eviction/scheduling-framework/)
      * [Dynamic Resource Allocation](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)
      * [Gang Scheduling](/docs/concepts/scheduling-eviction/gang-scheduling/)
      * [Scheduler Performance Tuning](/docs/concepts/scheduling-eviction/scheduler-perf-tuning/)
      * [PodGroup Scheduling](/docs/concepts/scheduling-eviction/podgroup-scheduling/)
      * [Resource Bin Packing](/docs/concepts/scheduling-eviction/resource-bin-packing/)
      * [Workload-Aware Preemption](/docs/concepts/scheduling-eviction/workload-aware-preemption/)
      * [Pod Priority and Preemption](/docs/concepts/scheduling-eviction/pod-priority-preemption/)
      * [Node-pressure Eviction](/docs/concepts/scheduling-eviction/node-pressure-eviction/)
      * [API-initiated Eviction](/docs/concepts/scheduling-eviction/api-eviction/)
      * [Node Declared Features](/docs/concepts/scheduling-eviction/node-declared-features/)
    - [Cluster Administration](/docs/concepts/cluster-administration/)
      * [Node Shutdowns](/docs/concepts/cluster-administration/node-shutdown/)
      * [Swap memory management](/docs/concepts/cluster-administration/swap-memory-management/)
      * [Node Autoscaling](/docs/concepts/cluster-administration/node-autoscaling/)
      * [Certificates](/docs/concepts/cluster-administration/certificates/)
      * [Cluster Networking](/docs/concepts/cluster-administration/networking/)
      * [Observability](/docs/concepts/cluster-administration/observability/)
      * [Admission Webhook Good Practices](/docs/concepts/cluster-administration/admission-webhooks-good-practices/)
      * [Good practices for Dynamic Resource Allocation as a Cluster Admin](/docs/concepts/cluster-administration/dra/)
      * [Logging Architecture](/docs/concepts/cluster-administration/logging/)
      * [Compatibility Version For Kubernetes Control Plane Components](/docs/concepts/cluster-administration/compatibility-version/)
      * [Metrics For Kubernetes System Components](/docs/concepts/cluster-administration/system-metrics/)
      * [Metrics for Kubernetes Object States](/docs/concepts/cluster-administration/kube-state-metrics/)
      * [System Logs](/docs/concepts/cluster-administration/system-logs/)
      * [Traces For Kubernetes System Components](/docs/concepts/cluster-administration/system-traces/)
      * [Proxies in Kubernetes](/docs/concepts/cluster-administration/proxies/)
      * [API Priority and Fairness](/docs/concepts/cluster-administration/flow-control/)
      * [Installing Addons](/docs/concepts/cluster-administration/addons/)
      * [Coordinated Leader Election](/docs/concepts/cluster-administration/coordinated-leader-election/)
    - [Windows in Kubernetes](/docs/concepts/windows/)
      * [Windows containers in Kubernetes](/docs/concepts/windows/intro/)
      * [Guide for Running Windows Containers in Kubernetes](/docs/concepts/windows/user-guide/)
    - [Extending Kubernetes](/docs/concepts/extend-kubernetes/)
      * [Compute, Storage, and Networking Extensions](/docs/concepts/extend-kubernetes/compute-storage-net/)
        + [Network Plugins](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
        + [Device Plugins](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
      * [Extending the Kubernetes API](/docs/concepts/extend-kubernetes/api-extension/)
        + [Custom Resources](/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
        + [Kubernetes API Aggregation Layer](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)
      * [Operator pattern](/docs/concepts/extend-kubernetes/operator/)
  + [Tasks](/docs/tasks/)
    - [Install Tools](/docs/tasks/tools/)
      * [Install and Set Up kubectl on Linux](/docs/tasks/tools/install-kubectl-linux/)
      * [Install and Set Up kubectl on macOS](/docs/tasks/tools/install-kubectl-macos/)
      * [Install and Set Up kubectl on Windows](/docs/tasks/tools/install-kubectl-windows/)
    - [Administer a Cluster](/docs/tasks/administer-cluster/)
      * [Administration with kubeadm](/docs/tasks/administer-cluster/kubeadm/)
        + [Adding Linux worker nodes](/docs/tasks/administer-cluster/kubeadm/adding-linux-nodes/)
        + [Adding Windows worker nodes](/docs/tasks/administer-cluster/kubeadm/adding-windows-nodes/)
        + [Upgrading kubeadm clusters](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
        + [Upgrading Linux nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/)
        + [Upgrading Windows nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/)
        + [Configuring a cgroup driver](/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/)
        + [Certificate Management with kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/)
        + [Reconfiguring a kubeadm cluster](/docs/tasks/administer-cluster/kubeadm/kubeadm-reconfigure/)
        + [Changing The Kubernetes Package Repository](/docs/tasks/administer-cluster/kubeadm/change-package-repository/)
      * [Overprovision Node Capacity For A Cluster](/docs/tasks/administer-cluster/node-overprovisioning/)
      * [Migrating from dockershim](/docs/tasks/administer-cluster/migrating-from-dockershim/)
        + [Changing the Container Runtime on a Node from Docker Engine to containerd](/docs/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd/)
        + [Find Out What Container Runtime is Used on a Node](/docs/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use/)
        + [Troubleshooting CNI plugin-related errors](/docs/tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors/)
        + [Check whether dockershim removal affects you](/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/)
        + [Migrating telemetry and security agents from dockershim](/docs/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents/)
      * [Generate Certificates Manually](/docs/tasks/administer-cluster/certificates/)
      * [Manage Memory, CPU, and API Resources](/docs/tasks/administer-cluster/manage-resources/)
        + [Configure Default Memory Requests and Limits for a Namespace](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)
        + [Configure Default CPU Requests and Limits for a Namespace](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)
        + [Configure Minimum and Maximum Memory Constraints for a Namespace](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)
        + [Configure Minimum and Maximum CPU Constraints for a Namespace](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)
        + [Configure Memory and CPU Quotas for a Namespace](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)
        + [Configure a Pod Quota for a Namespace](/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)
      * [Install a Network Policy Provider](/docs/tasks/administer-cluster/network-policy-provider/)
        + [Use Antrea for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/antrea-network-policy/)
        + [Use Calico for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/calico-network-policy/)
        + [Use Cilium for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/cilium-network-policy/)
        + [Use Kube-router for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/kube-router-network-policy/)
        + [Romana for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/romana-network-policy/)
        + [Weave Net for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/weave-network-policy/)
      * [Access Clusters Using the Kubernetes API](/docs/tasks/administer-cluster/access-cluster-api/)
      * [Enable Or Disable Feature Gates](/docs/tasks/administer-cluster/configure-feature-gates/)
      * [Advertise Extended Resources for a Node](/docs/tasks/administer-cluster/extended-resource-node/)
      * [Autoscale the DNS Service in a Cluster](/docs/tasks/administer-cluster/dns-horizontal-autoscaling/)
      * [Change the Access Mode of a PersistentVolume to ReadWriteOncePod](/docs/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod/)
      * [Change the default StorageClass](/docs/tasks/administer-cluster/change-default-storage-class/)
      * [Switching from Polling to CRI Event-based Updates to Container Status](/docs/tasks/administer-cluster/switch-to-evented-pleg/)
      * [Change the Reclaim Policy of a PersistentVolume](/docs/tasks/administer-cluster/change-pv-reclaim-policy/)
      * [Cloud Controller Manager Administration](/docs/tasks/administer-cluster/running-cloud-controller/)
      * [Configure a kubelet image credential provider](/docs/tasks/administer-cluster/kubelet-credential-provider/)
      * [Configure Quotas for API Objects](/docs/tasks/administer-cluster/quota-api-object/)
      * [Control CPU Management Policies on the Node](/docs/tasks/administer-cluster/cpu-management-policies/)
      * [Control Memory Management Policies on a Node](/docs/tasks/administer-cluster/memory-manager/)
      * [Control Topology Management Policies on a node](/docs/tasks/administer-cluster/topology-manager/)
      * [Customizing DNS Service](/docs/tasks/administer-cluster/dns-custom-nameservers/)
      * [Debugging DNS Resolution](/docs/tasks/administer-cluster/dns-debugging-resolution/)
      * [Declare Network Policy](/docs/tasks/administer-cluster/declare-network-policy/)
      * [Developing Cloud Controller Manager](/docs/tasks/administer-cluster/developing-cloud-controller-manager/)
      * [Enable Or Disable A Kubernetes API](/docs/tasks/administer-cluster/enable-disable-api/)
      * [Encrypting Confidential Data at Rest](/docs/tasks/administer-cluster/encrypt-data/)
      * [Decrypt Confidential Data that is Already Encrypted at Rest](/docs/tasks/administer-cluster/decrypt-data/)
      * [Guaranteed Scheduling For Critical Add-On Pods](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/)
      * [IP Masquerade Agent User Guide](/docs/tasks/administer-cluster/ip-masq-agent/)
      * [Limit Storage Consumption](/docs/tasks/administer-cluster/limit-storage-consumption/)
      * [Migrate Replicated Control Plane To Use Cloud Controller Manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/)
      * [Operating etcd clusters for Kubernetes](/docs/tasks/administer-cluster/configure-upgrade-etcd/)
      * [Reserve Compute Resources for System Daemons](/docs/tasks/administer-cluster/reserve-compute-resources/)
      * [Running Kubernetes Node Components as a Non-root User](/docs/tasks/administer-cluster/kubelet-in-userns/)
      * [Safely Drain a Node](/docs/tasks/administer-cluster/safely-drain-node/)
      * [Securing a Cluster](/docs/tasks/administer-cluster/securing-a-cluster/)
      * [Harden Dynamic Resource Allocation in Your Cluster](/docs/tasks/administer-cluster/hardening-dra/)
      * [Set Kubelet Parameters Via A Configuration File](/docs/tasks/administer-cluster/kubelet-config-file/)
      * [Share a Cluster with Namespaces](/docs/tasks/administer-cluster/namespaces/)
      * [Upgrade A Cluster](/docs/tasks/administer-cluster/cluster-upgrade/)
      * [Use Cascading Deletion in a Cluster](/docs/tasks/administer-cluster/use-cascading-deletion/)
      * [Using a KMS provider for data encryption](/docs/tasks/administer-cluster/kms-provider/)
      * [Using CoreDNS for Service Discovery](/docs/tasks/administer-cluster/coredns/)
      * [Using NodeLocal DNSCache in Kubernetes Clusters](/docs/tasks/administer-cluster/nodelocaldns/)
      * [Using sysctls in a Kubernetes Cluster](/docs/tasks/administer-cluster/sysctl-cluster/)
      * [Verify Signed Kubernetes Artifacts](/docs/tasks/administer-cluster/verify-signed-artifacts/)
    - [Configure Pods and Containers](/docs/tasks/configure-pod-container/)
      * [Assign Memory Resources to Containers and Pods](/docs/tasks/configure-pod-container/assign-memory-resource/)
      * [Assign CPU Resources to Containers and Pods](/docs/tasks/configure-pod-container/assign-cpu-resource/)
      * [Assign Devices to Pods and Containers](/docs/tasks/configure-pod-container/assign-resources/)
        + [Set Up DRA in a Cluster](/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster/)
        + [Allocate Devices to Workloads with DRA](/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/)
        + [Access DRA Device Metadata](/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/)
      * [Assign Pod-level CPU and memory resources](/docs/tasks/configure-pod-container/assign-pod-level-resources/)
      * [Configure GMSA for Windows Pods and containers](/docs/tasks/configure-pod-container/configure-gmsa/)
      * [Resize CPU and Memory Resources assigned to Containers](/docs/tasks/configure-pod-container/resize-container-resources/)
      * [Resize CPU and Memory Resources assigned to Pods](/docs/tasks/configure-pod-container/resize-pod-resources/)
      * [Configure RunAsUserName for Windows pods and containers](/docs/tasks/configure-pod-container/configure-runasusername/)
      * [Create a Windows HostProcess Pod](/docs/tasks/configure-pod-container/create-hostprocess-pod/)
      * [Configure Quality of Service for Pods](/docs/tasks/configure-pod-container/quality-service-pod/)
      * [Assign Extended Resources to a Container](/docs/tasks/configure-pod-container/extended-resource/)
      * [Configure a Pod to Use a Volume for Storage](/docs/tasks/configure-pod-container/configure-volume-storage/)
      * [Configure a Pod to Use a Projected Volume for Storage](/docs/tasks/configure-pod-container/configure-projected-volume-storage/)
      * [Configure a Security Context for a Pod or Container](/docs/tasks/configure-pod-container/security-context/)
      * [Configure Service Accounts for Pods](/docs/tasks/configure-pod-container/configure-service-account/)
      * [Pull an Image from a Private Registry](/docs/tasks/configure-pod-container/pull-image-private-registry/)
      * [Configure Liveness, Readiness and Startup Probes](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
      * [Assign Pods to Nodes](/docs/tasks/configure-pod-container/assign-pods-nodes/)
      * [Assign Pods to Nodes using Node Affinity](/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)
      * [Configure Pod Initialization](/docs/tasks/configure-pod-container/configure-pod-initialization/)
      * [Attach Handlers to Container Lifecycle Events](/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/)
      * [Configure a Pod to Use a ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/)
      * [Share Process Namespace between Containers in a Pod](/docs/tasks/configure-pod-container/share-process-namespace/)
      * [Use a User Namespace With a Pod](/docs/tasks/configure-pod-container/user-namespaces/)
      * [Use an Image Volume With a Pod](/docs/tasks/configure-pod-container/image-volumes/)
      * [Create static Pods](/docs/tasks/configure-pod-container/static-pod/)
      * [Translate a Docker Compose File to Kubernetes Resources](/docs/tasks/configure-pod-container/translate-compose-kubernetes/)
      * [Enforce Pod Security Standards by Configuring the Built-in Admission Controller](/docs/tasks/configure-pod-container/enforce-standards-admission-controller/)
      * [Enforce Pod Security Standards with Namespace Labels](/docs/tasks/configure-pod-container/enforce-standards-namespace-labels/)
      * [Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller](/docs/tasks/configure-pod-container/migrate-from-psp/)
    - [Monitoring, Logging, and Debugging](/docs/tasks/debug/)
      * [Logging in Kubernetes](/docs/tasks/debug/logging/)
      * [Monitoring in Kubernetes](/docs/tasks/debug/monitoring/)
      * [Troubleshooting Applications](/docs/tasks/debug/debug-application/)
        + [Debug Pods](/docs/tasks/debug/debug-application/debug-pods/)
        + [Debug Services](/docs/tasks/debug/debug-application/debug-service/)
        + [Debug a StatefulSet](/docs/tasks/debug/debug-application/debug-statefulset/)
        + [Determine the Reason for Pod Failure](/docs/tasks/debug/debug-application/determine-reason-pod-failure/)
        + [Debug Init Containers](/docs/tasks/debug/debug-application/debug-init-containers/)
        + [Debug Running Pods](/docs/tasks/debug/debug-application/debug-running-pod/)
        + [Get a Shell to a Running Container](/docs/tasks/debug/debug-application/get-shell-running-container/)
      * [Troubleshooting Clusters](/docs/tasks/debug/debug-cluster/)
        + [Troubleshooting kubectl](/docs/tasks/debug/debug-cluster/troubleshoot-kubectl/)
        + [Resource metrics pipeline](/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/)
        + [Tools for Monitoring Resources](/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
        + [Monitor Node Health](/docs/tasks/debug/debug-cluster/monitor-node-health/)
        + [Debugging Kubernetes nodes with crictl](/docs/tasks/debug/debug-cluster/crictl/)
        + [Troubleshooting Topology Management](/docs/tasks/debug/debug-cluster/topology/)
        + [Auditing](/docs/tasks/debug/debug-cluster/audit/)
        + [Debugging Kubernetes Nodes With Kubectl](/docs/tasks/debug/debug-cluster/kubectl-node-debug/)
        + [Developing and debugging services locally using telepresence](/docs/tasks/debug/debug-cluster/local-debugging/)
        + [Windows debugging tips](/docs/tasks/debug/debug-cluster/windows/)
    - [Manage Kubernetes Objects](/docs/tasks/manage-kubernetes-objects/)
      * [Declarative Management of Kubernetes Objects Using Configuration Files](/docs/tasks/manage-kubernetes-objects/declarative-config/)
      * [Declarative Management of Kubernetes Objects Using Kustomize](/docs/tasks/manage-kubernetes-objects/kustomization/)
      * [Managing Kubernetes Objects Using Imperative Commands](/docs/tasks/manage-kubernetes-objects/imperative-command/)
      * [Imperative Management of Kubernetes Objects Using Configuration Files](/docs/tasks/manage-kubernetes-objects/imperative-config/)
      * [Update API Objects in Place Using kubectl patch](/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/)
      * [Migrate Kubernetes Objects Using Storage Version Migration](/docs/tasks/manage-kubernetes-objects/storage-version-migration/)
    - [Managing Secrets](/docs/tasks/configmap-secret/)
      * [Managing Secrets using kubectl](/docs/tasks/configmap-secret/managing-secret-using-kubectl/)
      * [Managing Secrets using Configuration File](/docs/tasks/configmap-secret/managing-secret-using-config-file/)
      * [Managing Secrets using Kustomize](/docs/tasks/configmap-secret/managing-secret-using-kustomize/)
    - [Inject Data Into Applications](/docs/tasks/inject-data-application/)
      * [Define a Command and Arguments for a Container](/docs/tasks/inject-data-application/define-command-argument-container/)
      * [Define Dependent Environment Variables](/docs/tasks/inject-data-application/define-interdependent-environment-variables/)
      * [Define Environment Variables for a Container](/docs/tasks/inject-data-application/define-environment-variable-container/)
      * [Define Environment Variable Values Using An Init Container](/docs/tasks/inject-data-application/define-environment-variable-via-file/)
      * [Expose Pod Information to Containers Through Environment Variables](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)
      * [Expose Pod Information to Containers Through Files](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)
      * [Distribute Credentials Securely Using Secrets](/docs/tasks/inject-data-application/distribute-credentials-secure/)
    - [Run Applications](/docs/tasks/run-application/)
      * [Run a Stateless Application Using a Deployment](/docs/tasks/run-application/run-stateless-application-deployment/)
      * [Horizontal Manual Scaling for a Deployment](/docs/tasks/run-application/scale-deployment/)
      * [Update a Deployment Without Downtime](/docs/tasks/run-application/update-deployment-rolling/)
      * [Run a Single-Instance Stateful Application](/docs/tasks/run-application/run-single-instance-stateful-application/)
      * [Run a Replicated Stateful Application](/docs/tasks/run-application/run-replicated-stateful-application/)
      * [Scale a StatefulSet](/docs/tasks/run-application/scale-stateful-set/)
      * [Delete a StatefulSet](/docs/tasks/run-application/delete-stateful-set/)
      * [Force Delete StatefulSet Pods](/docs/tasks/run-application/force-delete-stateful-set-pod/)
      * [HorizontalPodAutoscaler Walkthrough](/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)
      * [Specifying a Disruption Budget for your Application](/docs/tasks/run-application/configure-pdb/)
      * [Accessing the Kubernetes API from a Pod](/docs/tasks/run-application/access-api-from-pod/)
    - [Run Jobs](/docs/tasks/job/)
      * [Running Automated Tasks with a CronJob](/docs/tasks/job/automated-tasks-with-cron-jobs/)
      * [Coarse Parallel Processing Using a Work Queue](/docs/tasks/job/coarse-parallel-processing-work-queue/)
      * [Fine Parallel Processing Using a Work Queue](/docs/tasks/job/fine-parallel-processing-work-queue/)
      * [Indexed Job for Parallel Processing with Static Work Assignment](/docs/tasks/job/indexed-parallel-processing-static/)
      * [Job with Pod-to-Pod Communication](/docs/tasks/job/job-with-pod-to-pod-communication/)
      * [Parallel Processing using Expansions](/docs/tasks/job/parallel-processing-expansion/)
      * [Handling retriable and non-retriable pod failures with Pod failure policy](/docs/tasks/job/pod-failure-policy/)
    - [Access Applications in a Cluster](/docs/tasks/access-application-cluster/)
      * [Deploy and Access the Kubernetes Dashboard](/docs/tasks/access-application-cluster/web-ui-dashboard/)
      * [Accessing Clusters](/docs/tasks/access-application-cluster/access-cluster/)
      * [Configure Access to Multiple Clusters](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)
      * [Use Port Forwarding to Access Applications in a Cluster](/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)
      * [Use a Service to Access an Application in a Cluster](/docs/tasks/access-application-cluster/service-access-application-cluster/)
      * [Connect a Frontend to a Backend Using Services](/docs/tasks/access-application-cluster/connecting-frontend-backend/)
      * [Create an External Load Balancer](/docs/tasks/access-application-cluster/create-external-load-balancer/)
      * [List All Container Images Running in a Cluster](/docs/tasks/access-application-cluster/list-all-running-container-images/)
      * [Communicate Between Containers in the Same Pod Using a Shared Volume](/docs/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume/)
      * [Configure DNS for a Cluster](/docs/tasks/access-application-cluster/configure-dns-cluster/)
      * [Access Services Running on Clusters](/docs/tasks/access-application-cluster/access-cluster-services/)
    - [Extend Kubernetes](/docs/tasks/extend-kubernetes/)
      * [Configure the Aggregation Layer](/docs/tasks/extend-kubernetes/configure-aggregation-layer/)
      * [Use Custom Resources](/docs/tasks/extend-kubernetes/custom-resources/)
        + [Extend the Kubernetes API with CustomResourceDefinitions](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)
        + [Versions in CustomResourceDefinitions](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/)
      * [Set up an Extension API Server](/docs/tasks/extend-kubernetes/setup-extension-api-server/)
      * [Configure Multiple Schedulers](/docs/tasks/extend-kubernetes/configure-multiple-schedulers/)
      * [Use an HTTP Proxy to Access the Kubernetes API](/docs/tasks/extend-kubernetes/http-proxy-access-api/)
      * [Use a SOCKS5 Proxy to Access the Kubernetes API](/docs/tasks/extend-kubernetes/socks5-proxy-access-api/)
      * [Set up Konnectivity service](/docs/tasks/extend-kubernetes/setup-konnectivity/)
    - [TLS](/docs/tasks/tls/)
      * [Issue a Certificate for a Kubernetes API Client Using A CertificateSigningRequest](/docs/tasks/tls/certificate-issue-client-csr/)
      * [Configure Certificate Rotation for the Kubelet](/docs/tasks/tls/certificate-rotation/)
      * [Manage TLS Certificates in a Cluster](/docs/tasks/tls/managing-tls-in-a-cluster/)
      * [Manual Rotation of CA Certificates](/docs/tasks/tls/manual-rotation-of-ca-certificates/)
    - [Manage Cluster Daemons](/docs/tasks/manage-daemon/)
      * [Building a Basic DaemonSet](/docs/tasks/manage-daemon/create-daemon-set/)
      * [Perform a Rolling Update on a DaemonSet](/docs/tasks/manage-daemon/update-daemon-set/)
      * [Perform a Rollback on a DaemonSet](/docs/tasks/manage-daemon/rollback-daemon-set/)
      * [Running Pods on Only Some Nodes](/docs/tasks/manage-daemon/pods-some-nodes/)
    - [Networking](/docs/tasks/network/)
      * [Adding entries to Pod /etc/hosts with HostAliases](/docs/tasks/network/customize-hosts-file-for-pods/)
      * [Extend Service IP Ranges](/docs/tasks/network/extend-service-ip-ranges/)
      * [Kubernetes Default ServiceCIDR Reconfiguration](/docs/tasks/network/reconfigure-default-service-ip-ranges/)
      * [Validate IPv4/IPv6 dual-stack](/docs/tasks/network/validate-dual-stack/)
    - [Extend kubectl with plugins](/docs/tasks/extend-kubectl/kubectl-plugins/)
    - [Manage HugePages](/docs/tasks/manage-hugepages/scheduling-hugepages/)
    - [Schedule GPUs](/docs/tasks/manage-gpus/scheduling-gpus/)
  + [Tutorials](/docs/tutorials/)
    - [Hello Minikube](/docs/tutorials/hello-minikube/)
    - [Learn Kubernetes Basics](/docs/tutorials/kubernetes-basics/)
      * [Create a Cluster](/docs/tutorials/kubernetes-basics/create-cluster/)
        + [Using Minikube to Create a Cluster](/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/)
      * [Deploy an App](/docs/tutorials/kubernetes-basics/deploy-app/)
        + [Using kubectl to Create a Deployment](/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)
      * [Explore Your App](/docs/tutorials/kubernetes-basics/explore/)
        + [Viewing Pods and Nodes](/docs/tutorials/kubernetes-basics/explore/explore-intro/)
      * [Expose Your App Publicly](/docs/tutorials/kubernetes-basics/expose/)
        + [Using a Service to Expose Your App](/docs/tutorials/kubernetes-basics/expose/expose-intro/)
      * [Scale Your App](/docs/tutorials/kubernetes-basics/scale/)
        + [Running Multiple Instances of Your App](/docs/tutorials/kubernetes-basics/scale/scale-intro/)
      * [Update Your App](/docs/tutorials/kubernetes-basics/update/)
        + [Performing a Rolling Update](/docs/tutorials/kubernetes-basics/update/update-intro/)
    - [Configuration](/docs/tutorials/configuration/)
      * [Updating Configuration via a ConfigMap](/docs/tutorials/configuration/updating-configuration-via-a-configmap/)
      * [Configuring Redis using a ConfigMap](/docs/tutorials/configuration/configure-redis-using-configmap/)
      * [Adopting Sidecar Containers](/docs/tutorials/configuration/pod-sidecar-containers/)
      * [Configure a Pod to Use a PersistentVolume for Storage](/docs/tutorials/configuration/configure-persistent-volume-storage/)
    - [Security](/docs/tutorials/security/)
      * [Apply Pod Security Standards at the Cluster Level](/docs/tutorials/security/cluster-level-pss/)
      * [Apply Pod Security Standards at the Namespace Level](/docs/tutorials/security/ns-level-pss/)
      * [Restrict a Container's Access to Resources with AppArmor](/docs/tutorials/security/apparmor/)
      * [Restrict a Container's Syscalls with seccomp](/docs/tutorials/security/seccomp/)
    - [Stateless Applications](/docs/tutorials/stateless-application/)
      * [Exposing an External IP Address to Access an Application in a Cluster](/docs/tutorials/stateless-application/expose-external-ip-address/)
      * [Example: Deploying PHP Guestbook application with Redis](/docs/tutorials/stateless-application/guestbook/)
    - [Stateful Applications](/docs/tutorials/stateful-application/)
      * [StatefulSet Basics](/docs/tutorials/stateful-application/basic-stateful-set/)
      * [Example: Deploying WordPress and MySQL with Persistent Volumes](/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/)
      * [Example: Deploying Cassandra with a StatefulSet](/docs/tutorials/stateful-application/cassandra/)
      * [Running ZooKeeper, A Distributed System Coordinator](/docs/tutorials/stateful-application/zookeeper/)
    - [Cluster Management](/docs/tutorials/cluster-management/)
      * [Running Kubelet in Standalone Mode](/docs/tutorials/cluster-management/kubelet-standalone/)
      * [Configuring swap memory on Kubernetes nodes](/docs/tutorials/cluster-management/provision-swap-memory/)
      * [Install Drivers and Allocate Devices with DRA](/docs/tutorials/cluster-management/install-use-dra/)
      * [Namespaces Walkthrough](/docs/tutorials/cluster-management/namespaces-walkthrough/)
    - [Services](/docs/tutorials/services/)
      * [Connecting Applications with Services](/docs/tutorials/services/connect-applications-service/)
      * [Using Source IP](/docs/tutorials/services/source-ip/)
      * [Explore Termination Behavior for Pods And Their Endpoints](/docs/tutorials/services/pods-and-endpoint-termination-flow/)
  + [Reference](/docs/reference/)
    - [Glossary](/docs/reference/glossary/)
    - [API Overview](/docs/reference/using-api/)
      * [Declarative API Validation](/docs/reference/using-api/declarative-validation/)
      * [Kubernetes API Concepts](/docs/reference/using-api/api-concepts/)
      * [Server-Side Apply](/docs/reference/using-api/server-side-apply/)
      * [Client Libraries](/docs/reference/using-api/client-libraries/)
      * [Common Expression Language in Kubernetes](/docs/reference/using-api/cel/)
      * [Kubernetes Deprecation Policy](/docs/reference/using-api/deprecation-policy/)
      * [Deprecated API Migration Guide](/docs/reference/using-api/deprecation-guide/)
      * [Kubernetes API health endpoints](/docs/reference/using-api/health-checks/)
    - [API Access Control](/docs/reference/access-authn-authz/)
      * [Authenticating](/docs/reference/access-authn-authz/authentication/)
      * [Authenticating with Bootstrap Tokens](/docs/reference/access-authn-authz/bootstrap-tokens/)
      * [Authorization](/docs/reference/access-authn-authz/authorization/)
      * [Using RBAC Authorization](/docs/reference/access-authn-authz/rbac/)
      * [Using Node Authorization](/docs/reference/access-authn-authz/node/)
      * [Webhook Mode](/docs/reference/access-authn-authz/webhook/)
      * [Using ABAC Authorization](/docs/reference/access-authn-authz/abac/)
      * [Admission Control](/docs/reference/access-authn-authz/admission-controllers/ "Admission Control in Kubernetes")
      * [Dynamic Admission Control](/docs/reference/access-authn-authz/extensible-admission-controllers/)
      * [Managing Service Accounts](/docs/reference/access-authn-authz/service-accounts-admin/)
      * [User Impersonation](/docs/reference/access-authn-authz/user-impersonation/)
      * [Certificates and Certificate Signing Requests](/docs/reference/access-authn-authz/certificate-signing-requests/)
      * [Mapping PodSecurityPolicies to Pod Security Standards](/docs/reference/access-authn-authz/psp-to-pod-security-standards/)
      * [Kubelet authentication/authorization](/docs/reference/access-authn-authz/kubelet-authn-authz/)
      * [TLS bootstrapping](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)
      * [Manifest-Based Admission Control](/docs/reference/access-authn-authz/manifest-admission-control/)
      * [Mutating Admission Policy](/docs/reference/access-authn-authz/mutating-admission-policy/)
      * [Validating Admission Policy](/docs/reference/access-authn-authz/validating-admission-policy/)
    - [Well-Known Labels, Annotations and Taints](/docs/reference/labels-annotations-taints/)
      * [Audit Annotations](/docs/reference/labels-annotations-taints/audit-annotations/)
    - [Kubernetes API](/docs/reference/kubernetes-api/)
      * [Workload Resources](/docs/reference/kubernetes-api/workload-resources/)
        + [Pod](/docs/reference/kubernetes-api/workload-resources/pod-v1/)
        + [Binding](/docs/reference/kubernetes-api/workload-resources/binding-v1/)
        + [PodTemplate](/docs/reference/kubernetes-api/workload-resources/pod-template-v1/)
        + [PodGroup v1alpha2](/docs/reference/kubernetes-api/workload-resources/pod-group-v1alpha2/)
        + [ReplicationController](/docs/reference/kubernetes-api/workload-resources/replication-controller-v1/)
        + [ReplicaSet](/docs/reference/kubernetes-api/workload-resources/replica-set-v1/)
        + [Deployment](/docs/reference/kubernetes-api/workload-resources/deployment-v1/)
        + [StatefulSet](/docs/reference/kubernetes-api/workload-resources/stateful-set-v1/)
        + [ControllerRevision](/docs/reference/kubernetes-api/workload-resources/controller-revision-v1/)
        + [DaemonSet](/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/)
        + [Job](/docs/reference/kubernetes-api/workload-resources/job-v1/)
        + [CronJob](/docs/reference/kubernetes-api/workload-resources/cron-job-v1/)
        + [HorizontalPodAutoscaler](/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/)
        + [HorizontalPodAutoscaler](/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2/)
        + [PriorityClass](/docs/reference/kubernetes-api/workload-resources/priority-class-v1/)
        + [DeviceTaintRule v1beta2](/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1beta2/)
        + [ResourceClaim](/docs/reference/kubernetes-api/workload-resources/resource-claim-v1/)
        + [ResourceClaimTemplate](/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/)
        + [ResourceSlice](/docs/reference/kubernetes-api/workload-resources/resource-slice-v1/)
        + [Workload v1alpha2](/docs/reference/kubernetes-api/workload-resources/workload-v1alpha2/)
      * [Service Resources](/docs/reference/kubernetes-api/service-resources/)
        + [Service](/docs/reference/kubernetes-api/service-resources/service-v1/)
        + [Endpoints](/docs/reference/kubernetes-api/service-resources/endpoints-v1/)
        + [EndpointSlice](/docs/reference/kubernetes-api/service-resources/endpoint-slice-v1/)
        + [Ingress](/docs/reference/kubernetes-api/service-resources/ingress-v1/)
        + [IngressClass](/docs/reference/kubernetes-api/service-resources/ingress-class-v1/)
      * [Config and Storage Resources](/docs/reference/kubernetes-api/config-and-storage-resources/)
        + [ConfigMap](/docs/reference/kubernetes-api/config-and-storage-resources/config-map-v1/)
        + [Secret](/docs/reference/kubernetes-api/config-and-storage-resources/secret-v1/)
        + [CSIDriver](/docs/reference/kubernetes-api/config-and-storage-resources/csi-driver-v1/)
        + [CSINode](/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/)
        + [CSIStorageCapacity](/docs/reference/kubernetes-api/config-and-storage-resources/csi-storage-capacity-v1/)
        + [PersistentVolumeClaim](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/)
        + [PersistentVolume](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/)
        + [StorageClass](/docs/reference/kubernetes-api/config-and-storage-resources/storage-class-v1/)
        + [StorageVersionMigration v1beta1](/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1beta1/)
        + [Volume](/docs/reference/kubernetes-api/config-and-storage-resources/volume/)
        + [VolumeAttachment](/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/)
        + [VolumeAttributesClass](/docs/reference/kubernetes-api/config-and-storage-resources/volume-attributes-class-v1/)
      * [Authentication Resources](/docs/reference/kubernetes-api/authentication-resources/)
        + [ServiceAccount](/docs/reference/kubernetes-api/authentication-resources/service-account-v1/)
        + [TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
        + [TokenReview](/docs/reference/kubernetes-api/authentication-resources/token-review-v1/)
        + [CertificateSigningRequest](/docs/reference/kubernetes-api/authentication-resources/certificate-signing-request-v1/)
        + [ClusterTrustBundle v1beta1](/docs/reference/kubernetes-api/authentication-resources/cluster-trust-bundle-v1beta1/)
        + [SelfSubjectReview](/docs/reference/kubernetes-api/authentication-resources/self-subject-review-v1/)
        + [PodCertificateRequest v1beta1](/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1beta1/)
      * [Authorization Resources](/docs/reference/kubernetes-api/authorization-resources/)
        + [LocalSubjectAccessReview](/docs/reference/kubernetes-api/authorization-resources/local-subject-access-review-v1/)
        + [SelfSubjectAccessReview](/docs/reference/kubernetes-api/authorization-resources/self-subject-access-review-v1/)
        + [SelfSubjectRulesReview](/docs/reference/kubernetes-api/authorization-resources/self-subject-rules-review-v1/)
        + [SubjectAccessReview](/docs/reference/kubernetes-api/authorization-resources/subject-access-review-v1/)
        + [ClusterRole](/docs/reference/kubernetes-api/authorization-resources/cluster-role-v1/)
        + [ClusterRoleBinding](/docs/reference/kubernetes-api/authorization-resources/cluster-role-binding-v1/)
        + [Role](/docs/reference/kubernetes-api/authorization-resources/role-v1/)
        + [RoleBinding](/docs/reference/kubernetes-api/authorization-resources/role-binding-v1/)
      * [Policy Resources](/docs/reference/kubernetes-api/policy-resources/)
        + [FlowSchema](/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/)
        + [LimitRange](/docs/reference/kubernetes-api/policy-resources/limit-range-v1/)
        + [ResourceQuota](/docs/reference/kubernetes-api/policy-resources/resource-quota-v1/)
        + [NetworkPolicy](/docs/reference/kubernetes-api/policy-resources/network-policy-v1/)
        + [PodDisruptionBudget](/docs/reference/kubernetes-api/policy-resources/pod-disruption-budget-v1/)
        + [PriorityLevelConfiguration](/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/)
        + [ValidatingAdmissionPolicy](/docs/reference/kubernetes-api/policy-resources/validating-admission-policy-v1/)
        + [ValidatingAdmissionPolicyBinding](/docs/reference/kubernetes-api/policy-resources/validating-admission-policy-binding-v1/)
        + [MutatingAdmissionPolicy](/docs/reference/kubernetes-api/policy-resources/mutating-admission-policy-v1/)
        + [MutatingAdmissionPolicyBinding](/docs/reference/kubernetes-api/policy-resources/mutating-admission-policy-binding-v1/)
      * [Extend Resources](/docs/reference/kubernetes-api/extend-resources/)
        + [CustomResourceDefinition](/docs/reference/kubernetes-api/extend-resources/custom-resource-definition-v1/)
        + [DeviceClass](/docs/reference/kubernetes-api/extend-resources/device-class-v1/)
        + [MutatingWebhookConfiguration](/docs/reference/kubernetes-api/extend-resources/mutating-webhook-configuration-v1/)
        + [ValidatingWebhookConfiguration](/docs/reference/kubernetes-api/extend-resources/validating-webhook-configuration-v1/)
      * [Cluster Resources](/docs/reference/kubernetes-api/cluster-resources/)
        + [APIService](/docs/reference/kubernetes-api/cluster-resources/api-service-v1/)
        + [ComponentStatus](/docs/reference/kubernetes-api/cluster-resources/component-status-v1/)
        + [Event](/docs/reference/kubernetes-api/cluster-resources/event-v1/)
        + [IPAddress](/docs/reference/kubernetes-api/cluster-resources/ip-address-v1/)
        + [Lease](/docs/reference/kubernetes-api/cluster-resources/lease-v1/)
        + [LeaseCandidate v1beta1](/docs/reference/kubernetes-api/cluster-resources/lease-candidate-v1beta1/)
        + [Namespace](/docs/reference/kubernetes-api/cluster-resources/namespace-v1/)
        + [Node](/docs/reference/kubernetes-api/cluster-resources/node-v1/)
        + [RuntimeClass](/docs/reference/kubernetes-api/cluster-resources/runtime-class-v1/)
        + [ResourcePoolStatusRequest v1alpha3](/docs/reference/kubernetes-api/cluster-resources/resource-pool-status-request-v1alpha3/)
        + [ServiceCIDR](/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/)
      * [Common Definitions](/docs/reference/kubernetes-api/common-definitions/)
        + [DeleteOptions](/docs/reference/kubernetes-api/common-definitions/delete-options/)
        + [LabelSelector](/docs/reference/kubernetes-api/common-definitions/label-selector/)
        + [ListMeta](/docs/reference/kubernetes-api/common-definitions/list-meta/)
        + [LocalObjectReference](/docs/reference/kubernetes-api/common-definitions/local-object-reference/)
        + [NodeSelectorRequirement](/docs/reference/kubernetes-api/common-definitions/node-selector-requirement/)
        + [ObjectFieldSelector](/docs/reference/kubernetes-api/common-definitions/object-field-selector/)
        + [ObjectMeta](/docs/reference/kubernetes-api/common-definitions/object-meta/)
        + [ObjectReference](/docs/reference/kubernetes-api/common-definitions/object-reference/)
        + [Patch](/docs/reference/kubernetes-api/common-definitions/patch/)
        + [Quantity](/docs/reference/kubernetes-api/common-definitions/quantity/)
        + [ResourceFieldSelector](/docs/reference/kubernetes-api/common-definitions/resource-field-selector/)
        + [Status](/docs/reference/kubernetes-api/common-definitions/status/)
        + [TypedLocalObjectReference](/docs/reference/kubernetes-api/common-definitions/typed-local-object-reference/)
      * [Common Parameters](/docs/reference/kubernetes-api/common-parameters/common-parameters/)
    - [Instrumentation](/docs/reference/instrumentation/)
      * [Service Level Indicator Metrics](/docs/reference/instrumentation/slis/ "Kubernetes Component SLI Metrics")
      * [CRI Pod & Container Metrics](/docs/reference/instrumentation/cri-pod-container-metrics/)
      * [Native Histograms](/docs/reference/instrumentation/native-histograms/ "Native Histogram Support for Kubernetes Metrics")
      * [Node metrics data](/docs/reference/instrumentation/node-metrics/)
      * [Understand Pressure Stall Information (PSI) Metrics](/docs/reference/instrumentation/understand-psi-metrics/)
      * [Kubernetes z-pages](/docs/reference/instrumentation/zpages/)
      * [Kubernetes Metrics Reference](/docs/reference/instrumentation/metrics/)
    - [Kubernetes Issues and Security](/docs/reference/issues-security/)
      * [Kubernetes Issue Tracker](/docs/reference/issues-security/issues/)
      * [Kubernetes Security and Disclosure Information](/docs/reference/issues-security/security/)
      * [CVE feed](/docs/reference/issues-security/official-cve-feed/ "Official CVE Feed")
    - [Node Reference Information](/docs/reference/node/)
      * [Kubelet Checkpoint API](/docs/reference/node/kubelet-checkpoint-api/)
      * [Linux Kernel Version Requirements](/docs/reference/node/kernel-version-requirements/)
      * [Articles on dockershim Removal and on Using CRI-compatible Runtimes](/docs/reference/node/topics-on-dockershim-and-cri-compatible-runtimes/)
      * [Kubelet Pod Info gRPC API](/docs/reference/node/kubelet-pod-info-grpc-api/)
      * [Node Labels Populated By The Kubelet](/docs/reference/node/node-labels/)
      * [Kubelet Sync Loop](/docs/reference/node/kubelet-sync-loop/)
      * [Local Files And Paths Used By The Kubelet](/docs/reference/node/kubelet-files/)
      * [Kubelet Configuration Directory Merging](/docs/reference/node/kubelet-config-directory-merging/)
      * [Kubelet Device Manager API Versions](/docs/reference/node/device-plugin-api-versions/)
      * [Kubelet Systemd Watchdog](/docs/reference/node/systemd-watchdog/)
      * [Node Status](/docs/reference/node/node-status/)
      * [Seccomp and Kubernetes](/docs/reference/node/seccomp/)
      * [Linux Node Swap Behaviors](/docs/reference/node/swap-behavior/)
    - [Networking Reference](/docs/reference/networking/)
      * [Protocols for Services](/docs/reference/networking/service-protocols/)
      * [Ports and Protocols](/docs/reference/networking/ports-and-protocols/)
      * [Virtual IPs and Service Proxies](/docs/reference/networking/virtual-ips/)
    - [Setup tools](/docs/reference/setup-tools/)
      * [Kubeadm](/docs/reference/setup-tools/kubeadm/)
        + [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/)
        + [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/)
        + [kubeadm upgrade](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/)
        + [kubeadm upgrade phases](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade-phase/)
        + [kubeadm config](/docs/reference/setup-tools/kubeadm/kubeadm-config/)
        + [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/)
        + [kubeadm token](/docs/reference/setup-tools/kubeadm/kubeadm-token/)
        + [kubeadm version](/docs/reference/setup-tools/kubeadm/kubeadm-version/)
        + [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/)
        + [kubeadm certs](/docs/reference/setup-tools/kubeadm/kubeadm-certs/)
        + [kubeadm init phase](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/)
        + [kubeadm join phase](/docs/reference/setup-tools/kubeadm/kubeadm-join-phase/)
        + [kubeadm kubeconfig](/docs/reference/setup-tools/kubeadm/kubeadm-kubeconfig/)
        + [kubeadm reset phase](/docs/reference/setup-tools/kubeadm/kubeadm-reset-phase/)
        + [Implementation details](/docs/reference/setup-tools/kubeadm/implementation-details/)
    - [Command line tool (kubectl)](/docs/reference/kubectl/)
      * [Introduction to kubectl](/docs/reference/kubectl/introduction/)
      * [kubectl Quick Reference](/docs/reference/kubectl/quick-reference/)
      * [kubectl reference](/docs/reference/kubectl/generated/)
        + [kubectl](/docs/reference/kubectl/generated/kubectl/)
        + [kubectl annotate](/docs/reference/kubectl/generated/kubectl_annotate/)
        + [kubectl api-resources](/docs/reference/kubectl/generated/kubectl_api-resources/)
        + [kubectl api-versions](/docs/reference/kubectl/generated/kubectl_api-versions/)
        + [kubectl apply](/docs/reference/kubectl/generated/kubectl_apply/)
          - [kubectl apply edit-last-applied](/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_edit-last-applied/)
          - [kubectl apply set-last-applied](/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_set-last-applied/)
          - [kubectl apply view-last-applied](/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_view-last-applied/)
        + [kubectl attach](/docs/reference/kubectl/generated/kubectl_attach/)
        + [kubectl auth](/docs/reference/kubectl/generated/kubectl_auth/)
          - [kubectl auth can-i](/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_can-i/)
          - [kubectl auth reconcile](/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_reconcile/)
          - [kubectl auth whoami](/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_whoami/)
        + [kubectl autoscale](/docs/reference/kubectl/generated/kubectl_autoscale/)
        + [kubectl certificate](/docs/reference/kubectl/generated/kubectl_certificate/)
          - [kubectl certificate approve](/docs/reference/kubectl/generated/kubectl_certificate/kubectl_certificate_approve/)
          - [kubectl certificate deny](/docs/reference/kubectl/generated/kubectl_certificate/kubectl_certificate_deny/)
        + [kubectl cluster-info](/docs/reference/kubectl/generated/kubectl_cluster-info/)
          - [kubectl cluster-info dump](/docs/reference/kubectl/generated/kubectl_cluster-info/kubectl_cluster-info_dump/)
        + [kubectl completion](/docs/reference/kubectl/generated/kubectl_completion/)
        + [kubectl config](/docs/reference/kubectl/generated/kubectl_config/)
          - [kubectl config current-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_current-context/)
          - [kubectl config delete-cluster](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-cluster/)
          - [kubectl config delete-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-context/)
          - [kubectl config delete-user](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-user/)
          - [kubectl config get-clusters](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-clusters/)
          - [kubectl config get-contexts](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-contexts/)
          - [kubectl config get-users](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-users/)
          - [kubectl config rename-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_rename-context/)
          - [kubectl config set](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set/)
          - [kubectl config set-cluster](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-cluster/)
          - [kubectl config set-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-context/)
          - [kubectl config set-credentials](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-credentials/)
          - [kubectl config unset](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_unset/)
          - [kubectl config use-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_use-context/)
          - [kubectl config view](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_view/)
        + [kubectl cordon](/docs/reference/kubectl/generated/kubectl_cordon/)
        + [kubectl cp](/docs/reference/kubectl/generated/kubectl_cp/)
        + [kubectl create](/docs/reference/kubectl/generated/kubectl_create/)
          - [kubectl create clusterrole](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_clusterrole/)
          - [kubectl create clusterrolebinding](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_clusterrolebinding/)
          - [kubectl create configmap](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_configmap/)
          - [kubectl create cronjob](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_cronjob/)
          - [kubectl create deployment](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_deployment/)
          - [kubectl create ingress](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_ingress/)
          - [kubectl create job](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_job/)
          - [kubectl create namespace](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_namespace/)
          - [kubectl create poddisruptionbudget](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_poddisruptionbudget/)
          - [kubectl create priorityclass](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_priorityclass/)
          - [kubectl create quota](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_quota/)
          - [kubectl create role](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_role/)
          - [kubectl create rolebinding](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_rolebinding/)
          - [kubectl create secret](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret/)
          - [kubectl create secret docker-registry](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_docker-registry/)
          - [kubectl create secret generic](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_generic/)
          - [kubectl create secret tls](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_tls/)
          - [kubectl create service](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service/)
          - [kubectl create service clusterip](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_clusterip/)
          - [kubectl create service externalname](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_externalname/)
          - [kubectl create service loadbalancer](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_loadbalancer/)
          - [kubectl create service nodeport](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_nodeport/)
          - [kubectl create serviceaccount](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_serviceaccount/)
          - [kubectl create token](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_token/)
        + [kubectl debug](/docs/reference/kubectl/generated/kubectl_debug/)
        + [kubectl delete](/docs/reference/kubectl/generated/kubectl_delete/)
        + [kubectl describe](/docs/reference/kubectl/generated/kubectl_describe/)
        + [kubectl diff](/docs/reference/kubectl/generated/kubectl_diff/)
        + [kubectl drain](/docs/reference/kubectl/generated/kubectl_drain/)
        + [kubectl edit](/docs/reference/kubectl/generated/kubectl_edit/)
        + [kubectl events](/docs/reference/kubectl/generated/kubectl_events/)
        + [kubectl exec](/docs/reference/kubectl/generated/kubectl_exec/)
        + [kubectl explain](/docs/reference/kubectl/generated/kubectl_explain/)
        + [kubectl expose](/docs/reference/kubectl/generated/kubectl_expose/)
        + [kubectl get](/docs/reference/kubectl/generated/kubectl_get/)
        + [kubectl kuberc](/docs/reference/kubectl/generated/kubectl_kuberc/)
          - [kubectl kuberc set](/docs/reference/kubectl/generated/kubectl_kuberc/kubectl_kuberc_set/)
          - [kubectl kuberc view](/docs/reference/kubectl/generated/kubectl_kuberc/kubectl_kuberc_view/)
        + [kubectl kustomize](/docs/reference/kubectl/generated/kubectl_kustomize/)
        + [kubectl label](/docs/reference/kubectl/generated/kubectl_label/)
        + [kubectl logs](/docs/reference/kubectl/generated/kubectl_logs/)
        + [kubectl options](/docs/reference/kubectl/generated/kubectl_options/)
        + [kubectl patch](/docs/reference/kubectl/generated/kubectl_patch/)
        + [kubectl plugin](/docs/reference/kubectl/generated/kubectl_plugin/)
          - [kubectl plugin list](/docs/reference/kubectl/generated/kubectl_plugin/kubectl_plugin_list/)
        + [kubectl port-forward](/docs/reference/kubectl/generated/kubectl_port-forward/)
        + [kubectl proxy](/docs/reference/kubectl/generated/kubectl_proxy/)
        + [kubectl replace](/docs/reference/kubectl/generated/kubectl_replace/)
        + [kubectl rollout](/docs/reference/kubectl/generated/kubectl_rollout/)
          - [kubectl rollout history](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_history/)
          - [kubectl rollout pause](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_pause/)
          - [kubectl rollout restart](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_restart/)
          - [kubectl rollout resume](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_resume/)
          - [kubectl rollout status](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/)
          - [kubectl rollout undo](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_undo/)
        + [kubectl run](/docs/reference/kubectl/generated/kubectl_run/)
        + [kubectl scale](/docs/reference/kubectl/generated/kubectl_scale/)
        + [kubectl set](/docs/reference/kubectl/generated/kubectl_set/)
          - [kubectl set env](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_env/)
          - [kubectl set image](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_image/)
          - [kubectl set resources](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_resources/)
          - [kubectl set selector](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_selector/)
          - [kubectl set serviceaccount](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_serviceaccount/)
          - [kubectl set subject](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_subject/)
        + [kubectl taint](/docs/reference/kubectl/generated/kubectl_taint/)
        + [kubectl top](/docs/reference/kubectl/generated/kubectl_top/)
          - [kubectl top node](/docs/reference/kubectl/generated/kubectl_top/kubectl_top_node/)
          - [kubectl top pod](/docs/reference/kubectl/generated/kubectl_top/kubectl_top_pod/)
        + [kubectl uncordon](/docs/reference/kubectl/generated/kubectl_uncordon/)
        + [kubectl version](/docs/reference/kubectl/generated/kubectl_version/)
        + [kubectl wait](/docs/reference/kubectl/generated/kubectl_wait/)
      * [kubectl Commands](/docs/reference/kubectl/kubectl-cmds/)
      * [kubectl](/docs/reference/kubectl/kubectl/)
      * [JSONPath Support](/docs/reference/kubectl/jsonpath/)
      * [kubectl for Docker Users](/docs/reference/kubectl/docker-cli-to-kubectl/)
      * [kubectl Usage Conventions](/docs/reference/kubectl/conventions/)
      * [Kubectl user preferences (kuberc)](/docs/reference/kubectl/kuberc/)
    - [Encodings](/docs/reference/encodings/)
      * [KYAML Reference](/docs/reference/encodings/kyaml/)
    - [Component tools](/docs/reference/command-line-tools-reference/)
      * [Feature Gates](/docs/reference/command-line-tools-reference/feature-gates/)
      * [Feature Gates (removed)](/docs/reference/command-line-tools-reference/feature-gates-removed/)
      * [kube-apiserver](/docs/reference/command-line-tools-reference/kube-apiserver/)
      * [kube-controller-manager](/docs/reference/command-line-tools-reference/kube-controller-manager/)
      * [kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/)
      * [kube-scheduler](/docs/reference/command-line-tools-reference/kube-scheduler/)
      * [kubelet](/docs/reference/command-line-tools-reference/kubelet/)
    - [Debug cluster](/docs/reference/debug-cluster/)
      * [Flow control](/docs/reference/debug-cluster/flow-control/)
    - [Configuration APIs](/docs/reference/config-api/)
      * [Client Authentication (v1)](/docs/reference/config-api/client-authentication.v1/)
      * [Client Authentication (v1beta1)](/docs/reference/config-api/client-authentication.v1beta1/)
      * [Event Rate Limit Configuration (v1alpha1)](/docs/reference/config-api/apiserver-eventratelimit.v1alpha1/)
      * [Image Policy API (v1alpha1)](/docs/reference/config-api/imagepolicy.v1alpha1/)
      * [kube-apiserver Admission (v1)](/docs/reference/config-api/apiserver-admission.v1/)
      * [kube-apiserver Audit Configuration (v1)](/docs/reference/config-api/apiserver-audit.v1/)
      * [kube-apiserver Configuration (v1)](/docs/reference/config-api/apiserver-config.v1/)
      * [kube-apiserver Configuration (v1alpha1)](/docs/reference/config-api/apiserver-config.v1alpha1/)
      * [kube-apiserver Configuration (v1beta1)](/docs/reference/config-api/apiserver-config.v1beta1/)
      * [kube-controller-manager Configuration (v1alpha1)](/docs/reference/config-api/kube-controller-manager-config.v1alpha1/)
      * [kube-proxy Configuration (v1alpha1)](/docs/reference/config-api/kube-proxy-config.v1alpha1/)
      * [kube-scheduler Configuration (v1)](/docs/reference/config-api/kube-scheduler-config.v1/)
      * [kubeadm Configuration (v1beta3)](/docs/reference/config-api/kubeadm-config.v1beta3/)
      * [kubeadm Configuration (v1beta4)](/docs/reference/config-api/kubeadm-config.v1beta4/)
      * [kubeconfig (v1)](/docs/reference/config-api/kubeconfig.v1/)
      * [Kubelet Configuration (v1)](/docs/reference/config-api/kubelet-config.v1/)
      * [Kubelet Configuration (v1alpha1)](/docs/reference/config-api/kubelet-config.v1alpha1/)
      * [Kubelet Configuration (v1beta1)](/docs/reference/config-api/kubelet-config.v1beta1/)
      * [Kubelet CredentialProvider (v1)](/docs/reference/config-api/kubelet-credentialprovider.v1/)
      * [kuberc (v1alpha1)](/docs/reference/config-api/kuberc.v1alpha1/)
      * [kuberc (v1beta1)](/docs/reference/config-api/kuberc.v1beta1/)
      * [WebhookAdmission Configuration (v1)](/docs/reference/config-api/apiserver-webhookadmission.v1/)
    - [External APIs](/docs/reference/external-api/)
      * [Kubernetes Custom Metrics (v1beta2)](/docs/reference/external-api/custom-metrics.v1beta2/)
      * [Kubernetes External Metrics (v1beta1)](/docs/reference/external-api/external-metrics.v1beta1/)
      * [Kubernetes Metrics (v1beta1)](/docs/reference/external-api/metrics.v1beta1/)
    - [Scheduling](/docs/reference/scheduling/)
      * [Scheduler Configuration](/docs/reference/scheduling/config/)
      * [Scheduling Policies](/docs/reference/scheduling/policies/)
    - [Other Tools](/docs/reference/tools/)
  + [Contribute](/docs/contribute/ "Contribute to Kubernetes")
    - [Contribute to Kubernetes Documentation](/docs/contribute/docs/)
    - [Contributing to Kubernetes blogs](/docs/contribute/blog/)
      * [Submitting articles to Kubernetes blogs](/docs/contribute/blog/article-submission/)
      * [Blog guidelines](/docs/contribute/blog/guidelines/)
      * [Blog article mirroring](/docs/contribute/blog/article-mirroring/)
      * [Post-release communications](/docs/contribute/blog/release-comms/)
      * [Helping as a blog writing buddy](/docs/contribute/blog/writing-buddy/)
    - [Suggesting content improvements](/docs/contribute/suggesting-improvements/)
    - [Contributing new content](/docs/contribute/new-content/)
      * [Opening a pull request](/docs/contribute/new-content/open-a-pr/)
      * [Previewing locally](/docs/contribute/new-content/preview-locally/)
      * [Documenting for a release](/docs/contribute/new-content/new-features/ "Documenting a feature for a release")
      * [Case studies](/docs/contribute/new-content/case-studies/ "Submitting case studies")
    - [Reviewing changes](/docs/contribute/review/)
      * [Reviewing pull requests](/docs/contribute/review/reviewing-prs/)
      * [For approvers and reviewers](/docs/contribute/review/for-approvers/ "Reviewing for approvers and reviewers")
    - [Localizing Kubernetes documentation](/docs/contribute/localization/)
    - [Participating in SIG Docs](/docs/contribute/participate/)
      * [Roles and responsibilities](/docs/contribute/participate/roles-and-responsibilities/)
      * [Issue Wranglers](/docs/contribute/participate/issue-wrangler/)
      * [PR wranglers](/docs/contribute/participate/pr-wranglers/)
    - [Documentation style overview](/docs/contribute/style/)
      * [Content guide](/docs/contribute/style/content-guide/ "Documentation Content Guide")
      * [Style guide](/docs/contribute/style/style-guide/ "Documentation Style Guide")
      * [Diagram guide](/docs/contribute/style/diagram-guide/ "Diagram Guide")
      * [Writing a new topic](/docs/contribute/style/write-new-topic/)
      * [Page content types](/docs/contribute/style/page-content-types/)
      * [Content organization](/docs/contribute/style/content-organization/)
      * [Custom Hugo Shortcodes](/docs/contribute/style/hugo-shortcodes/)
    - [Updating Reference Documentation](/docs/contribute/generate-ref-docs/)
      * [Quickstart](/docs/contribute/generate-ref-docs/quickstart/ "Reference Documentation Quickstart")
      * [Contributing to the Upstream Kubernetes Code](/docs/contribute/generate-ref-docs/contribute-upstream/)
      * [Generating Reference Documentation for the Kubernetes API](/docs/contribute/generate-ref-docs/kubernetes-api/)
      * [Generating Reference Documentation for kubectl Commands](/docs/contribute/generate-ref-docs/kubectl/)
      * [Generating Reference Documentation for Metrics](/docs/contribute/generate-ref-docs/metrics-reference/)
      * [Generating Reference Pages for Kubernetes Components and Tools](/docs/contribute/generate-ref-docs/kubernetes-components/)
    - [Advanced contributing](/docs/contribute/advanced/)
    - [Viewing Site Analytics](/docs/contribute/analytics/)
  + [Docs smoke test page](/docs/test/)

[ReplicaSet API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/)
 [Edit this page](https://github.com/kubernetes/website/edit/main/content/en/docs/concepts/workloads/controllers/replicaset.md)
 [Create child page](https://github.com/kubernetes/website/new/main/content/en/docs/concepts/workloads/controllers/replicaset.md?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)
 [Create an issue](https://github.com/kubernetes/website/issues/new?title=ReplicaSet)
 [Print entire section](https://kubernetes.io/docs/concepts/workloads/controllers/_print/)

* [How a ReplicaSet works](#how-a-replicaset-works)
* [When to use a ReplicaSet](#when-to-use-a-replicaset)
* [Example](#example)
* [Non-Template Pod acquisitions](#non-template-pod-acquisitions)
* [Writing a ReplicaSet manifest](#writing-a-replicaset-manifest)
  + [Pod Template](#pod-template)
  + [Pod Selector](#pod-selector)
  + [Replicas](#replicas)
* [Working with ReplicaSets](#working-with-replicasets)
  + [Deleting a ReplicaSet and its Pods](#deleting-a-replicaset-and-its-pods)
  + [Deleting just a ReplicaSet](#deleting-just-a-replicaset)
  + [Terminating Pods](#terminating-pods)
  + [Isolating Pods from a ReplicaSet](#isolating-pods-from-a-replicaset)
  + [Scaling a ReplicaSet](#scaling-a-replicaset)
  + [Pod deletion cost](#pod-deletion-cost)
  + [ReplicaSet as a Horizontal Pod Autoscaler Target](#replicaset-as-a-horizontal-pod-autoscaler-target)
* [Alternatives to ReplicaSet](#alternatives-to-replicaset)
  + [Deployment (recommended)](#deployment-recommended)
  + [Bare Pods](#bare-pods)
  + [Job](#job)
  + [DaemonSet](#daemonset)
  + [ReplicationController](#replicationcontroller)
* [What's next](#what-s-next)

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Workloads](https://kubernetes.io/docs/concepts/workloads/)
4. [Workload Management](https://kubernetes.io/docs/concepts/workloads/controllers/)
5. [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)

# ReplicaSet

A ReplicaSet's purpose is to maintain a stable set of replica Pods running at any given time. Usually, you define a Deployment and let that Deployment manage ReplicaSets automatically.

A ReplicaSet's purpose is to maintain a stable set of replica Pods running at any given time. As such, it is often
used to guarantee the availability of a specified number of identical Pods.

## How a ReplicaSet works

A ReplicaSet is defined with fields, including a selector that specifies how to identify Pods it can acquire, a number
of replicas indicating how many Pods it should be maintaining, and a pod template specifying the data of new Pods
it should create to meet the number of replicas criteria. A ReplicaSet then fulfills its purpose by creating
and deleting Pods as needed to reach the desired number. When a ReplicaSet needs to create new Pods, it uses its Pod
template.

A ReplicaSet is linked to its Pods via the Pods' [metadata.ownerReferences](/docs/concepts/architecture/garbage-collection/#owners-dependents)
field, which specifies what resource the current object is owned by. All Pods acquired by a ReplicaSet have their owning
ReplicaSet's identifying information within their ownerReferences field. It's through this link that the ReplicaSet
knows of the state of the Pods it is maintaining and plans accordingly.

A ReplicaSet identifies new Pods to acquire by using its selector. If there is a Pod that has no
OwnerReference or the OwnerReference is not a [Controller](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") and it
matches a ReplicaSet's selector, it will be immediately acquired by said ReplicaSet.

## When to use a ReplicaSet

A ReplicaSet ensures that a specified number of pod replicas are running at any given
time. However, a Deployment is a higher-level concept that manages ReplicaSets and
provides declarative updates to Pods along with a lot of other useful features.
Therefore, we recommend using Deployments instead of directly using ReplicaSets, unless
you require custom update orchestration or don't require updates at all.

This actually means that you may never need to manipulate ReplicaSet objects:
use a Deployment instead, and define your application in the spec section.

## Example

[`controllers/frontend.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/controllers/frontend.yaml)![](/images/copycode.svg "Copy controllers/frontend.yaml to clipboard")

```
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: frontend
  labels:
    app: guestbook
    tier: frontend
spec:
  # modify replicas according to your case
  replicas: 3
  selector:
    matchLabels:
      tier: frontend
  template:
    metadata:
      labels:
        tier: frontend
    spec:
      containers:
      - name: php-redis
        image: us-docker.pkg.dev/google-samples/containers/gke/gb-frontend:v5
```

Saving this manifest into `frontend.yaml` and submitting it to a Kubernetes cluster will
create the defined ReplicaSet and the Pods that it manages.

```
kubectl apply -f https://kubernetes.io/examples/controllers/frontend.yaml
```

You can then get the current ReplicaSets deployed:

```
kubectl get rs
```

And see the frontend one you created:

```
NAME       DESIRED   CURRENT   READY   AGE
frontend   3         3         3       6s
```

You can also check on the state of the ReplicaSet:

```
kubectl describe rs/frontend
```

And you will see output similar to:

```
Name:         frontend
Namespace:    default
Selector:     tier=frontend
Labels:       app=guestbook
              tier=frontend
Annotations:  <none>
Replicas:     3 current / 3 desired
Pods Status:  3 Running / 0 Waiting / 0 Succeeded / 0 Failed
Pod Template:
  Labels:  tier=frontend
  Containers:
   php-redis:
    Image:        us-docker.pkg.dev/google-samples/containers/gke/gb-frontend:v5
    Port:         <none>
    Host Port:    <none>
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Events:
  Type    Reason            Age   From                   Message
  ----    ------            ----  ----                   -------
  Normal  SuccessfulCreate  13s   replicaset-controller  Created pod: frontend-gbgfx
  Normal  SuccessfulCreate  13s   replicaset-controller  Created pod: frontend-rwz57
  Normal  SuccessfulCreate  13s   replicaset-controller  Created pod: frontend-wkl7w
```

And lastly you can check for the Pods brought up:

```
kubectl get pods
```

You should see Pod information similar to:

```
NAME             READY   STATUS    RESTARTS   AGE
frontend-gbgfx   1/1     Running   0          10m
frontend-rwz57   1/1     Running   0          10m
frontend-wkl7w   1/1     Running   0          10m
```

You can also verify that the owner reference of these pods is set to the frontend ReplicaSet.
To do this, get the yaml of one of the Pods running:

```
kubectl get pods frontend-gbgfx -o yaml
```

The output will look similar to this, with the frontend ReplicaSet's info set in the metadata's ownerReferences field:

```
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: "2024-02-28T22:30:44Z"
  generateName: frontend-
  labels:
    tier: frontend
  name: frontend-gbgfx
  namespace: default
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: ReplicaSet
    name: frontend
    uid: e129deca-f864-481b-bb16-b27abfd92292
...
```

## Non-Template Pod acquisitions

While you can create bare Pods with no problems, it is strongly recommended to make sure that the bare Pods do not have
labels which match the selector of one of your ReplicaSets. The reason for this is because a ReplicaSet is not limited
to owning Pods specified by its template-- it can acquire other Pods in the manner specified in the previous sections.

Take the previous frontend ReplicaSet example, and the Pods specified in the following manifest:

[`pods/pod-rs.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/pod-rs.yaml)![](/images/copycode.svg "Copy pods/pod-rs.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: pod1
  labels:
    tier: frontend
spec:
  containers:
  - name: hello1
    image: gcr.io/google-samples/hello-app:2.0

---

apiVersion: v1
kind: Pod
metadata:
  name: pod2
  labels:
    tier: frontend
spec:
  containers:
  - name: hello2
    image: gcr.io/google-samples/hello-app:1.0
```

As those Pods do not have a Controller (or any object) as their owner reference and match the selector of the frontend
ReplicaSet, they will immediately be acquired by it.

Suppose you create the Pods after the frontend ReplicaSet has been deployed and has set up its initial Pod replicas to
fulfill its replica count requirement:

```
kubectl apply -f https://kubernetes.io/examples/pods/pod-rs.yaml
```

The new Pods will be acquired by the ReplicaSet, and then immediately terminated as the ReplicaSet would be over
its desired count.

Fetching the Pods:

```
kubectl get pods
```

The output shows that the new Pods are either already terminated, or in the process of being terminated:

```
NAME             READY   STATUS        RESTARTS   AGE
frontend-b2zdv   1/1     Running       0          10m
frontend-vcmts   1/1     Running       0          10m
frontend-wtsmm   1/1     Running       0          10m
pod1             0/1     Terminating   0          1s
pod2             0/1     Terminating   0          1s
```

If you create the Pods first:

```
kubectl apply -f https://kubernetes.io/examples/pods/pod-rs.yaml
```

And then create the ReplicaSet however:

```
kubectl apply -f https://kubernetes.io/examples/controllers/frontend.yaml
```

You shall see that the ReplicaSet has acquired the Pods and has only created new ones according to its spec until the
number of its new Pods and the original matches its desired count. As fetching the Pods:

```
kubectl get pods
```

Will reveal in its output:

```
NAME             READY   STATUS    RESTARTS   AGE
frontend-hmmj2   1/1     Running   0          9s
pod1             1/1     Running   0          36s
pod2             1/1     Running   0          36s
```

In this manner, a ReplicaSet can own a non-homogeneous set of Pods

## Writing a ReplicaSet manifest

As with all other Kubernetes API objects, a ReplicaSet needs the `apiVersion`, `kind`, and `metadata` fields.
For ReplicaSets, the `kind` is always a ReplicaSet.

When the control plane creates new Pods for a ReplicaSet, the `.metadata.name` of the
ReplicaSet is part of the basis for naming those Pods. The name of a ReplicaSet must be a valid
[DNS subdomain](/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names)
value, but this can produce unexpected results for the Pod hostnames. For best compatibility,
the name should follow the more restrictive rules for a
[DNS label](/docs/concepts/overview/working-with-objects/names/#dns-label-names).

A ReplicaSet also needs a [`.spec` section](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status).

### Pod Template

The `.spec.template` is a [pod template](/docs/concepts/workloads/pods/#pod-templates) which is also
required to have labels in place. In our `frontend.yaml` example we had one label: `tier: frontend`.
Be careful not to overlap with the selectors of other controllers, lest they try to adopt this Pod.

For the template's [restart policy](/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) field,
`.spec.template.spec.restartPolicy`, the only allowed value is `Always`, which is the default.

### Pod Selector

The `.spec.selector` field is a [label selector](/docs/concepts/overview/working-with-objects/labels/). As discussed
[earlier](#how-a-replicaset-works) these are the labels used to identify potential Pods to acquire. In our
`frontend.yaml` example, the selector was:

```
matchLabels:
  tier: frontend
```

In the ReplicaSet, `.spec.template.metadata.labels` must match `spec.selector`, or it will
be rejected by the API.

#### Note:

For 2 ReplicaSets specifying the same `.spec.selector` but different
`.spec.template.metadata.labels` and `.spec.template.spec` fields, each ReplicaSet ignores the
Pods created by the other ReplicaSet.

### Replicas

You can specify how many Pods should run concurrently by setting `.spec.replicas`. The ReplicaSet will create/delete
its Pods to match this number.

If you do not specify `.spec.replicas`, then it defaults to 1.

## Working with ReplicaSets

### Deleting a ReplicaSet and its Pods

To delete a ReplicaSet and all of its Pods, use
[`kubectl delete`](/docs/reference/generated/kubectl/kubectl-commands#delete). The
[Garbage collector](/docs/concepts/architecture/garbage-collection/) automatically deletes all of
the dependent Pods by default.

When using the REST API or the `client-go` library, you must set `propagationPolicy` to
`Background` or `Foreground` in the `-d` option. For example:

```
kubectl proxy --port=8080
curl -X DELETE  'localhost:8080/apis/apps/v1/namespaces/default/replicasets/frontend' \
  -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Foreground"}' \
  -H "Content-Type: application/json"
```

### Deleting just a ReplicaSet

You can delete a ReplicaSet without affecting any of its Pods using
[`kubectl delete`](/docs/reference/generated/kubectl/kubectl-commands#delete)
with the `--cascade=orphan` option.
When using the REST API or the `client-go` library, you must set `propagationPolicy` to `Orphan`.
For example:

```
kubectl proxy --port=8080
curl -X DELETE  'localhost:8080/apis/apps/v1/namespaces/default/replicasets/frontend' \
  -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Orphan"}' \
  -H "Content-Type: application/json"
```

Once the original is deleted, you can create a new ReplicaSet to replace it. As long
as the old and new `.spec.selector` are the same, then the new one will adopt the old Pods.
However, it will not make any effort to make existing Pods match a new, different pod template.
To update Pods to a new spec in a controlled way, use a
[Deployment](/docs/concepts/workloads/controllers/deployment/#creating-a-deployment), as
ReplicaSets do not support a rolling update directly.

### Terminating Pods

FEATURE STATE:
`Kubernetes v1.35 [beta]`(enabled by default)

You can enable this feature by setting the `DeploymentReplicaSetTerminatingReplicas`
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/)
on the [API server](/docs/reference/command-line-tools-reference/kube-apiserver/)
and on the [kube-controller-manager](/docs/reference/command-line-tools-reference/kube-controller-manager/)

Pods that become terminating due to deletion or scale down may take a long time to terminate, and may consume
additional resources during that period. As a result, the total number of all pods can temporarily exceed
`.spec.replicas`. Terminating pods can be tracked using the `.status.terminatingReplicas` field of the ReplicaSet.

### Isolating Pods from a ReplicaSet

You can remove Pods from a ReplicaSet by changing their labels. This technique may be used to remove Pods
from service for debugging, data recovery, etc. Pods that are removed in this way will be replaced automatically (
assuming that the number of replicas is not also changed).

### Scaling a ReplicaSet

A ReplicaSet can be easily scaled up or down by simply updating the `.spec.replicas` field. The ReplicaSet controller
ensures that a desired number of Pods with a matching label selector are available and operational.

When scaling down, the ReplicaSet controller chooses which pods to delete by sorting the available pods to
prioritize scaling down pods based on the following general algorithm:

1. Pending (and unschedulable) pods are scaled down first
2. If `controller.kubernetes.io/pod-deletion-cost` annotation is set, then
   the pod with the lower value will come first.
3. Pods on nodes with more replicas come before pods on nodes with fewer replicas.
4. If the pods' creation times differ, the pod that was created more recently
   comes before the older pod (the creation times are bucketed on an integer log scale).

If all of the above match, then selection is random.

### Pod deletion cost

FEATURE STATE:
`Kubernetes v1.22 [beta]`

Using the [`controller.kubernetes.io/pod-deletion-cost`](/docs/reference/labels-annotations-taints/#pod-deletion-cost)
annotation, users can set a preference regarding which pods to remove first when downscaling a ReplicaSet.

The annotation should be set on the pod, the range is [-2147483648, 2147483647]. It represents the cost of
deleting a pod compared to other pods belonging to the same ReplicaSet. Pods with lower deletion
cost are preferred to be deleted before pods with higher deletion cost.

The implicit value for this annotation for pods that don't set it is 0; negative values are permitted.
Invalid values will be rejected by the API server.

This feature is beta and enabled by default. You can disable it using the
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/)
`PodDeletionCost` in both kube-apiserver and kube-controller-manager.

#### Note:

* This is honored on a best-effort basis, so it does not offer any guarantees on pod deletion order.
* Users should avoid updating the annotation frequently, such as updating it based on a metric value,
  because doing so will generate a significant number of pod updates on the apiserver.

#### Example Use Case

The different pods of an application could have different utilization levels. On scale down, the application
may prefer to remove the pods with lower utilization. To avoid frequently updating the pods, the application
should update `controller.kubernetes.io/pod-deletion-cost` once before issuing a scale down (setting the
annotation to a value proportional to pod utilization level). This works if the application itself controls
the down scaling; for example, the driver pod of a Spark deployment.

### ReplicaSet as a Horizontal Pod Autoscaler Target

A ReplicaSet can also be a target for
[Horizontal Pod Autoscalers (HPA)](/docs/tasks/run-application/horizontal-pod-autoscale/). That is,
a ReplicaSet can be auto-scaled by an HPA. Here is an example HPA targeting
the ReplicaSet we created in the previous example.

[`controllers/hpa-rs.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/controllers/hpa-rs.yaml)![](/images/copycode.svg "Copy controllers/hpa-rs.yaml to clipboard")

```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: frontend-scaler
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: ReplicaSet
    name: frontend
  minReplicas: 3
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```

Saving this manifest into `hpa-rs.yaml` and submitting it to a Kubernetes cluster should
create the defined HPA that autoscales the target ReplicaSet depending on the CPU usage
of the replicated Pods.

```
kubectl apply -f https://k8s.io/examples/controllers/hpa-rs.yaml
```

Alternatively, you can use the `kubectl autoscale` command to accomplish the same
(and it's easier!)

```
kubectl autoscale rs frontend --max=10 --min=3 --cpu=50%
```

## Alternatives to ReplicaSet

### Deployment (recommended)

[`Deployment`](/docs/concepts/workloads/controllers/deployment/) is an object which can own ReplicaSets and update
them and their Pods via declarative, server-side rolling updates.
While ReplicaSets can be used independently, today they're mainly used by Deployments as a mechanism to orchestrate Pod
creation, deletion and updates. When you use Deployments you don't have to worry about managing the ReplicaSets that
they create. Deployments own and manage their ReplicaSets.
As such, it is recommended to use Deployments when you want ReplicaSets.

### Bare Pods

Unlike the case where a user directly created Pods, a ReplicaSet replaces Pods that are deleted or
terminated for any reason, such as in the case of node failure or disruptive node maintenance,
such as a kernel upgrade. For this reason, we recommend that you use a ReplicaSet even if your
application requires only a single Pod. Think of it similarly to a process supervisor, only it
supervises multiple Pods across multiple nodes instead of individual processes on a single node. A
ReplicaSet delegates local container restarts to some agent on the node such as Kubelet.

### Job

Use a [`Job`](/docs/concepts/workloads/controllers/job/) instead of a ReplicaSet for Pods that are
expected to terminate on their own (that is, batch jobs).

### DaemonSet

Use a [`DaemonSet`](/docs/concepts/workloads/controllers/daemonset/) instead of a ReplicaSet for Pods that provide a
machine-level function, such as machine monitoring or machine logging. These Pods have a lifetime that is tied
to a machine lifetime: the Pod needs to be running on the machine before other Pods start, and are
safe to terminate when the machine is otherwise ready to be rebooted/shutdown.

### ReplicationController

ReplicaSets are the successors to [ReplicationControllers](/docs/concepts/workloads/controllers/replicationcontroller/).
The two serve the same purpose, and behave similarly, except that a ReplicationController does not support set-based
selector requirements as described in the [labels user guide](/docs/concepts/overview/working-with-objects/labels/#label-selectors).
As such, ReplicaSets are preferred over ReplicationControllers

## What's next

* Learn about [Pods](/docs/concepts/workloads/pods/).
* Learn about [Deployments](/docs/concepts/workloads/controllers/deployment/).
* [Run a Stateless Application Using a Deployment](/docs/tasks/run-application/run-stateless-application-deployment/),
  which relies on ReplicaSets to work.
* `ReplicaSet` is a top-level resource in the Kubernetes REST API.
  Read the
  [ReplicaSet](/docs/reference/kubernetes-api/workload-resources/replica-set-v1/)
  object definition to understand the API for replica sets.
* Read about [PodDisruptionBudget](/docs/concepts/workloads/pods/disruptions/) and how
  you can use it to manage application availability during disruptions.

## Feedback

Was this page helpful?

Yes
No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on
[Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes).
Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to
[report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io)
or
[suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

  

Last modified September 26, 2025 at 6:20 PM PST: [Fix HPA CLI example in ReplicaSet doc (55add008ed)](https://github.com/kubernetes/website/commit/55add008edd6efd03de533257d4cf79628f58103)

© 2026 The Kubernetes Authors | Documentation Distributed under [CC BY 4.0](https://git.k8s.io/website/LICENSE)

© 2026 The Linux Foundation ®. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/trademark-usage)

ICP license: 京ICP备17074266号-3